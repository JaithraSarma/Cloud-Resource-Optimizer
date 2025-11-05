output "vm_names" {
  value = [for v in azurerm_linux_virtual_machine.vm : v.name]
}

output "resource_group" {
  value = azurerm_resource_group.rg.name
}

output "location" {
  value = azurerm_resource_group.rg.location
}
