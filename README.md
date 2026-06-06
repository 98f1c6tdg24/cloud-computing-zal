# IaC-cloud-lab
Azure IaC lab: GitHub + Terraform + Ansible from manual provisioning to full automation.

This repository demonstrates three approaches to Infrastructure as Code (IaC):

1. Manual Terraform deployment  - students inspect, adapt and run Terraform/Ansible files
2. GitHub-based IaC workflow, students clone the project from GitHub and provision infrastructure from code.

3. Fully automated provisioning with shell scripts - students run a shell script that provisions infrastructure and configures a simple Flask service

The lab uses Azure CLI, GitHub, Terraform and Ansible to provision and configure a Linux virtual machine running Flask

> The full automation path intentionally deploys Flask, not Apache. Apache configuration is left as a student task.

## Requirements

The recommended environment is **Azure Cloud Shell / Bash**.

Required tools:

- Azure CLI
- Git
- Terraform
- Ansible
- SSH client

## Quick start: full automation demo

```bash
az login
git clone https://github.com/magtk/iac-cloud-lab.git
cd iac-cloud-lab
chmod +x scripts/deploy.sh scripts/destroy.sh
./scripts/deploy.sh
```

Open the displayed address:

```text
http://PUBLIC_IP:5000
```

Destroy resources after the lab:

```bash
./scripts/destroy.sh
```

## Apache task

Apache configuration is not fully solved in the automation path. Students should complete:

```text
ansible/playbook-apache-task.yml
```

and verify the result at:

```text
http://PUBLIC_IP
```

## Repository structure

```text
iac-cloud-lab/
├── terraform/
│   ├── main.tf
│   └── outputs.tf
├── ansible/
│   ├── inventory.ini.template
│   ├── playbook-flask.yml
│   ├── playbook-apache-task.yml
│   └── files/
│       └── index.html.template
├── app/
│   ├── app.py
│   └── requirements.txt
├── scripts/
│   ├── deploy.sh
│   └── destroy.sh
└── .gitignore
```

