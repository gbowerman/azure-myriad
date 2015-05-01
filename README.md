# azure-myriad
Templates for VM Scale Sets. 

Note: VM Scale Sets are announced but not yet in preview:
- These templates will only work with whitelisted Azure subscriptions. 
  If your subscription hasn't been whitelisted for using VM Scale Sets, the resource type: Microsoft.Compute/virtualMachineScaleSets won't be recognized and the deployment will fail.
- API is not yet public and subject to breaking change.

### Limitations

This is pre-preview, with the following major limitations:

-	No load balancing
-	Single storage accounts for custom images
-	No command-line support for getting public IP addresses
-	No managed storage
-	Breaking changes will occur without notice
-	etc..

### Creating a VM Scale Set using PowerShell
 
Note: Specific imperative commands to manage scale sets are not implemented yet. The following commands manage templates where the VM Scale Sets are modelled.

Download <a href="http://az412849.vo.msecnd.net/downloads04/azure-powershell.0.9.0a.msi">PowerShell 0.9.0</a> or later.

Examples:
 
### Using an integrated template to create storage, VNET, Scale Set
 
Switch-AzureMode -Name AzureResourceManager
new-azureresourcegroup -name myrg -location 'West US'
new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateFile C:\ARM_Templates\VMSS\vmss-vnet-storage-win.json
Or
new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateUri https://raw.githubusercontent.com/gbowerman/azure-myriad/master/vmss-vnet-storage-ubuntu.json
 
### Get existing Scale Set details
 
Get-AzureResource -name myvmss -ResourceGroupName myrg -ResourceType Microsoft.Compute/virtualMachineScaleSets -ApiVersion 2014-12-01-preview
 
### Scale an existing VMSS in or out
 
new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateUri https://raw.githubusercontent.com/gbowerman/azure-myriad/master/vmss-scale-out-win.json

### Scale an existing VMSS in
new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateUri https://raw.githubusercontent.com/gbowerman/azure-myriad/master/vmss-scale-in.json
 
### Remove a VM Scale Set
 
Remove-AzureResource -Name myvmss -ResourceGroupName myrg -ApiVersion 2014-12-01-preview -ResourceType Microsoft.Compute/virtualMachineScaleSets
Or
Remove the Resource Group:
Remove-AzureResourceGroup -Name myrg


## Templates 

### vmss-vnet-storage-ubuntu.json

Creates a VNET, storage account, and scale set of identical Ubuntu virtual machines.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2F%2Fvmss-vnet-storage-ubuntu.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-scale-out-ubuntu.json

Create an Ubuntu VM Scale Set with an existing storage account and VNET, and change the number of instances. Used for scaling out.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2F%2Fvmss-scale-out-ubuntu.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-vnet-storage-win.json

Creates a VNET, storage account, and scale set of identical Windows virtual machines.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2F%2Fvmss-vnet-storage-win.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-scale-out-win.json

Create a Windows VM Scale Set with an existing storage account and VNET, and change the number of instances. Used for scaling out.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2F%2Fvmss-scale-out-win.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-vnet-storage-coreos.json

Creates a VNET, storage account, and scale set of identical CoreOS virtual machines.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2F%2Fvmss-vnet-storage-coreos.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-scale-out-coreos.json

Create a CoreOS VM Scale Set with an existing storage account and VNET, and change the number of instances. Used for scaling out.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2F%2Fvmss-scale-out-coreos.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-scale-in.json

Reduce the number of VM instances in a Scale Set (scale-in). Platform independent.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2F%2Fvmss-scale-in.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
