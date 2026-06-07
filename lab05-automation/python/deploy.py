#!/usr/bin/env python3
"""
Python orchestration script for iac-cloud-lab.

The script does not replace Terraform or Ansible.
It only runs them in the correct order.

It deploys the Flask container demo.
Apache remains a student task.
"""

from __future__ import annotations

import argparse
import os
import shutil
import socket
import subprocess
import sys
import time
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
TERRAFORM_DIR = ROOT_DIR / "lab03-terraform"
ANSIBLE_DIR = ROOT_DIR / "lab04-ansible"
INVENTORY_TEMPLATE = ANSIBLE_DIR / "inventory.ini.template"
INVENTORY_FILE = ANSIBLE_DIR / "inventory.ini"
SSH_PRIVATE_KEY = Path.home() / ".ssh" / "id_rsa"
SSH_PUBLIC_KEY = Path.home() / ".ssh" / "id_rsa.pub"


def run(command: list[str], cwd: Path | None = None, env: dict[str, str] | None = None) -> None:
    print(f"\n$ {' '.join(command)}")
    subprocess.run(command, cwd=cwd, env=env, check=True)


def capture(command: list[str], cwd: Path | None = None) -> str:
    print(f"\n$ {' '.join(command)}")
    result = subprocess.run(command, cwd=cwd, check=True, text=True, stdout=subprocess.PIPE)
    return result.stdout.strip()


def require_command(command_name: str) -> None:
    if shutil.which(command_name) is None:
        raise SystemExit(f"Brak wymaganego polecenia: {command_name}")


def check_required_tools() -> None:
    for command in ["az", "terraform", "ansible-playbook", "ssh-keygen"]:
        require_command(command)


def ensure_azure_login() -> None:
    try:
        subprocess.run(["az", "account", "show"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("Azure CLI: aktywne logowanie wykryte.")
    except subprocess.CalledProcessError:
        run(["az", "login"])


def ensure_ssh_key() -> None:
    if SSH_PUBLIC_KEY.exists():
        print(f"Klucz publiczny istnieje: {SSH_PUBLIC_KEY}")
        return
    SSH_PRIVATE_KEY.parent.mkdir(parents=True, exist_ok=True)
    run(["ssh-keygen", "-t", "rsa", "-b", "2048", "-N", "", "-f", str(SSH_PRIVATE_KEY)])


def terraform_apply(auto_approve: bool = True) -> str:
    run(["terraform", "init"], cwd=TERRAFORM_DIR)
    run(["terraform", "plan"], cwd=TERRAFORM_DIR)

    command = ["terraform", "apply"]
    if auto_approve:
        command.append("-auto-approve")
    run(command, cwd=TERRAFORM_DIR)

    return capture(["terraform", "output", "-raw", "vm_public_ip"], cwd=TERRAFORM_DIR)


def wait_for_port(host: str, port: int, timeout_seconds: int = 300) -> None:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        try:
            with socket.create_connection((host, port), timeout=5):
                print(f"Port {port} jest dostępny.")
                return
        except OSError:
            print(f"Czekam na {host}:{port} ...")
            time.sleep(5)
    raise TimeoutError(f"Port {port} na {host} nie stał się dostępny.")


def prepare_inventory(vm_ip: str) -> None:
    template = INVENTORY_TEMPLATE.read_text(encoding="utf-8")
    INVENTORY_FILE.write_text(template.replace("<PUBLIC_IP>", vm_ip), encoding="utf-8")


def run_ansible_flask_container() -> None:
    env = os.environ.copy()
    env["ANSIBLE_HOST_KEY_CHECKING"] = "False"
    run(["ansible-playbook", "-i", str(INVENTORY_FILE), "playbook-flask-container.yml"], cwd=ANSIBLE_DIR, env=env)


def main() -> int:
    parser = argparse.ArgumentParser(description="Deploy Azure VM and Flask container demo.")
    parser.add_argument("--no-auto-approve", action="store_true")
    parser.add_argument("--skip-ansible", action="store_true")
    args = parser.parse_args()

    try:
        check_required_tools()
        ensure_azure_login()
        ensure_ssh_key()

        vm_ip = terraform_apply(auto_approve=not args.no_auto_approve)
        print(f"Public IP: {vm_ip}")

        wait_for_port(vm_ip, 22)
        prepare_inventory(vm_ip)

        if not args.skip_ansible:
            run_ansible_flask_container()

        print("\n=== Gotowe ===")
        print(f"Flask container: http://{vm_ip}:5000")
        print(f"Apache task:     http://{vm_ip}")
        print("\nApache pozostaje zadaniem studenckim.")
        return 0

    except subprocess.CalledProcessError as error:
        print(f"Błąd polecenia: {error}", file=sys.stderr)
        return error.returncode or 1
    except Exception as error:
        print(f"Błąd: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
