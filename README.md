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

Repository URL used in the lab:

```bash
git clone https://github.com/magtk/iac-cloud-lab.git
```

This repository is a starter kit for a Cloud Technologies laboratory.

## Lab structure

```text
iac-cloud-lab/
├── lab01-nginx-aci/
├── lab02-flask-container/
├── lab03-terraform/
├── lab04-ansible/
└── lab05-automation/
```

## What students should see

- a ready-made container can be launched locally and in Azure,
- a simple Flask application can be containerized with Docker or Podman,
- cloud infrastructure can be created from code using Terraform,
- a VM can be configured using Ansible,
- deployment steps can be orchestrated with Bash or Python.

## Important

The automation examples deploy the Flask container demo.

Apache configuration is intentionally left as a student task in:

```text
lab04-ansible/playbook-apache-task.yml
```

## Cleanup

Always remove Azure resources after the lab:

```bash
cd lab03-terraform
terraform destroy -auto-approve
```

or use one of the destroy scripts from `lab05-automation`.

