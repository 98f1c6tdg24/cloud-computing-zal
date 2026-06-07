# LAB 4 – Ansible Apache task

This lab uses the VM created in `lab03-terraform`.

Prepare inventory:

```bash
cp inventory.ini.template inventory.ini
nano inventory.ini
```

Run Apache task:

```bash
ansible-playbook -i inventory.ini playbook-apache-task.yml
```

Apache playbook is intentionally incomplete.
Students should replace TODO tasks with proper Ansible modules.
