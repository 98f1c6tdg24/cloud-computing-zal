# LAB 5 – Automation

Automation scripts are two implementations of the same idea:

```text
Terraform creates infrastructure.
Ansible configures the VM.
Docker runs Flask as a container.
```

## Bash

```bash
cd lab05-automation/bash
chmod +x deploy.sh destroy.sh
./deploy.sh
```

Destroy:

```bash
./destroy.sh
```

## Python

```bash
cd lab05-automation/python
python3 deploy.py
```

Destroy:

```bash
python3 destroy.py
```

The Python script is not a replacement for Terraform or Ansible.
It only orchestrates command execution.
