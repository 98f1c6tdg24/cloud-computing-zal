# LAB 3 – Terraform Azure VM

This lab creates:

- Resource Group,
- Virtual Network,
- Subnet,
- Public IP,
- Network Security Group,
- Network Interface,
- Linux VM.

## Run

```bash
az login
terraform init
terraform plan
terraform apply -auto-approve
```

Get public IP:

```bash
terraform output -raw vm_public_ip
```

Cleanup:

```bash
terraform destroy -auto-approve
```
