# azure-myriad
Templates for Azure Virtual Machine Scale Sets. 

VM Scale Sets allow you to deploy and manage a group of identical virtual machines as a set. Advantages include:
-	Autoscale - simply change the instance count and Scale Sets will increase or decrease the number of VMs evenly across update and fault domains.
-	Performance - deploying hundreds of VMs results in a single call to the fabric, allowing inherent performance optimizations.
-	Customization - built on Azure IaaS, Scale Sets support all Windows and Linux VMs including custom images and extensions.
-	Ease of management - building on the simple declarative modelling introduced with Azure Resource Manager, Scale Sets are the simplest way to manage sets of identical VMs. Focus on compute at scale without managing scaling of storage accounts and NICs.

Note: VM Scale Sets are not yet in preview:
- These templates won't work until we start whitelisting Azure subscriptions. We've blocked all access while the dev team are busy making breaking changes to support updates and additions to the API. The example templates below are to provide an early view of the work. 

Preview update (8/31/15): Current plan is to start a private preview in October 2015, working with Azure Advisors. If you wish to participate in this preview, you can self-nominate <a href="http://aka.ms/vmadvisors">here</a>.  

### Limitations

This is preview, with the following major limitations:

-	Single storage accounts for custom images.
-	No image based patching support.
-	Breaking changes are possible.
-	etc..

### Creating a VM Scale Set using PowerShell
 
Note: Imperative commands to manage scale sets using CLI and PowerShell are being worked on. The following commands manage templates where the VM Scale Sets are modelled.

Download <a href="https://azure.microsoft.com/en-us/documentation/articles/powershell-install-configure/">Aure PowerShell 0.9.0</a> or later.

Examples:
 
### Using an integrated template to create storage, VNET, Scale Set
 
Switch-AzureMode -Name AzureResourceManager<br/>
new-azureresourcegroup -name myrg -location 'West US'<br/>
new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateUri https://raw.githubusercontent.com/gbowerman/azure-myriad/master/vmss-ubuntu-vnet-storage.json<br/>
Or refer to a file..<br/>
new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateFile C:\ARM_Templates\VMSS\vmss-win-vnet-storage.json<br/>
Or<br/>

 
### Get existing Scale Set details
 
Get-AzureResource -name myvmss -ResourceGroupName myrg -ResourceType Microsoft.Compute/virtualMachineScaleSets -ApiVersion 2015-05-01-preview
 
### Scale an existing VMSS in or out
 
new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateUri https://raw.githubusercontent.com/gbowerman/azure-myriad/master/vmss-scale-in-or-out.json

### Scale an existing VMSS in

new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateUri https://raw.githubusercontent.com/gbowerman/azure-myriad/master/vmss-scale-in-or-out.json
 
### Remove a VM Scale Set
 
Remove-AzureResource -Name myvmss -ResourceGroupName myrg -ApiVersion 2015-05-01-preview -ResourceType Microsoft.Compute/virtualMachineScaleSets<br/>
Or<br/>
Remove the Resource Group:<br/>
Remove-AzureResourceGroup -Name myrg<br/>


## Templates 

### vmss-ubuntu-vnet-storage.json

Creates a VNET, storage account, and scale set of identical Ubuntu virtual machines.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-ubuntu-vnet-storage.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-win-vnet-storage.json

Creates a VNET, storage account, and scale set of identical Windows virtual machines.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-win-vnet-storage.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-win-scale-out.json

Create a Windows VM Scale Set with an existing storage account and VNET, and change the number of instances. Used for scaling out.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-win-scale-out.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-coreos-vnet-storage.json

Creates a VNET, storage account, and scale set of identical CoreOS virtual machines.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-coreos-vnet-storage.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### mesos-vmss-simple-cluster.json

Create a simple mesos cluster with a single master, with a VM Scale Set of slaves.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fmesos-vmss-simple-cluster.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-scale-in-or-out.json

Reduce or increase the number of VM instances in a Scale Set. Platform independent.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-scale-in-or-out.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
