#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
TERRAFORM_DIR = ROOT_DIR / "lab03-terraform"


def require_command(command_name: str) -> None:
    if shutil.which(command_name) is None:
        raise SystemExit(f"Brak wymaganego polecenia: {command_name}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Destroy Terraform infrastructure.")
    parser.add_argument("--no-auto-approve", action="store_true")
    args = parser.parse_args()

    try:
        require_command("terraform")
        command = ["terraform", "destroy"]
        if not args.no_auto_approve:
            command.append("-auto-approve")
        subprocess.run(command, cwd=TERRAFORM_DIR, check=True)
        print("Infrastruktura została usunięta.")
        return 0
    except subprocess.CalledProcessError as error:
        print(f"Błąd polecenia: {error}", file=sys.stderr)
        return error.returncode or 1


if __name__ == "__main__":
    raise SystemExit(main())
