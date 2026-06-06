output "vm_public_ip" {
  value = azurerm_linux_virtual_machine.vm.public_ip_address
}

output "flask_url" {
  value = "http://${azurerm_linux_virtual_machine.vm.public_ip_address}:5000"
}

output "apache_url" {
  value = "http://${azurerm_linux_virtual_machine.vm.public_ip_address}"
}
