# azure-myriad
Ignite 2015 templates for Azure Virtual Machine Scale Sets. 

These templates are for demonstration purposes and have hardcoded values like sshKeyData which will not work without modification.

VM Scale Sets allow you to deploy and manage a group of identical virtual machines as a set. Advantages include:
-	Autoscale - simply change the instance count and Scale Sets will increase or decrease the number of VMs evenly across update and fault domains.
-	Performance - deploying hundreds of VMs results in a single call to the fabric, allowing inherent performance optimizations.
-	Customization - built on Azure IaaS, Scale Sets support all Windows and Linux VMs including custom images and extensions.
-	Ease of management - building on the simple declarative modelling introduced with Azure Resource Manager, Scale Sets are the simplest way to manage sets of identical VMs. Focus on compute at scale without managing scaling of storage accounts and NICs.

Note: VM Scale Sets are announced but not yet in preview:
- These templates will only work with whitelisted Azure subscriptions.<br/> 
  If your subscription hasn't been whitelisted for using VM Scale Sets, the resource type: <i>Microsoft.Compute/virtualMachineScaleSets</i> won't be recognized and the deployment will fail.
- API is not yet public and is subject to breaking change.

### Limitations

This is pre-preview, with the following major limitations:

-	No load balancing.
-	Single storage accounts for custom images.
-	No command-line support for getting public IP addresses.
-	No managed storage.
-	No image based patching support.
-	Breaking changes will occur without notice.
-	etc..

### Creating a VM Scale Set using PowerShell
 
Note: Specific imperative commands to manage scale sets are not implemented yet. The following commands manage templates where the VM Scale Sets are modelled.

Download <a href="http://az412849.vo.msecnd.net/downloads04/azure-powershell.0.9.0a.msi">PowerShell 0.9.0</a> or later.

Examples:
 
### Using an integrated template to create storage, VNET, Scale Set
 
Switch-AzureMode -Name AzureResourceManager<br/>
new-azureresourcegroup -name myrg -location 'West US'<br/>
new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateUri https://raw.githubusercontent.com/gbowerman/azure-myriad/master/vmss-ubuntu-vnet-storage.json<br/>
Or refer to a file..<br/>
new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateFile C:\ARM_Templates\VMSS\vmss-win-vnet-storage.json<br/>
Or<br/>

 
### Get existing Scale Set details
 
Get-AzureResource -name myvmss -ResourceGroupName myrg -ResourceType Microsoft.Compute/virtualMachineScaleSets -ApiVersion 2014-12-01-preview
 
### Scale an existing VMSS in or out
 
new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateUri https://raw.githubusercontent.com/gbowerman/azure-myriad/master/vmss-win-scale-out.json

### Scale an existing VMSS in

new-azureresourcegroupdeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateUri https://raw.githubusercontent.com/gbowerman/azure-myriad/master/vmss-scale-in.json
 
### Remove a VM Scale Set
 
Remove-AzureResource -Name myvmss -ResourceGroupName myrg -ApiVersion 2014-12-01-preview -ResourceType Microsoft.Compute/virtualMachineScaleSets<br/>
Or<br/>
Remove the Resource Group:<br/>
Remove-AzureResourceGroup -Name myrg<br/>


## Templates 

### mesos-crp-demo.json

Create a mesos master-slave configuration based on CoreOS VMs. Specify the number of Slave VMs.

Parameters: # Slave VMs, Region.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2fmaster%2Fignite2015%2Fmesos-crp-demo.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### mesos-vmss-demo.json

Create a mesos master-slave configuration based on CoreOS VMs. The slave VMs are part of a VM Scale Set to make it easier to scale up and down.

Parameters: # Slave VMs, Region.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fignite2015%2fmesos-vmss-demo.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-scale-in.json

Reduce the number of VM instances in a Scale Set (scale-in). Platform independent.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fignite2015%2Fvmss-scale-in.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>