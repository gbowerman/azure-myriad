# azure-myriad
Templates for Azure Virtual Machine Scale Sets. 

Note 10/6/15: All locations are enabled. Limited public preview has started.

If you wish to participate in this preview, your subscription needs to be whitelisted  to use the virtualMachineScaleSet Azure resource. You can self-nominate <a href="http://aka.ms/vmadvisors">here</a>.  

VM Scale Sets allow you to deploy and manage a group of identical virtual machines as a set. Advantages include:
-	Autoscale - simply change the instance count and Scale Sets will increase or decrease the number of VMs evenly across update and fault domains.
-	Performance - deploying multiple VMs results in a single call to the fabric, allowing inherent performance optimizations.
-	Customization - built on Azure IaaS, Scale Sets support all Windows and Linux VMs including custom images and extensions.
-	Ease of management - building on the simple declarative modelling introduced with Azure Resource Manager, Scale Sets are the simplest way to manage sets of identical VMs. Focus on compute at scale without managing scaling of storage accounts and NICs.


### Limitations

Please note the following limitations:

-	For custom images you can only have a single storage account and are hence limited to 40 VMs in a scale set. This will be increased in the future.
-	Maximum number of platform image VMs in a scale set is 100. This will be increased in the future.

## Working with scale sets using PowerShell

Note: Imperative commands to manage scale sets using CLI and PowerShell are being worked on. The following commands manage templates where the VM Scale Sets are modelled.

Download a recent <a href="https://azure.microsoft.com/en-us/documentation/articles/powershell-install-configure/">Aure PowerShell</a>.
 
You can deploy VMSS templates and query resources using any current Azure PowerShell version.

To get started switch to ARM and create a resource group (switching to ARM won't be needed with the latest PowerShell):

Switch-AzureMode -Name AzureResourceManager New-AzureResourcegroup -name myrg -location 'Southeast Asia'

###	Create a scale set
New-AzureResourceGroupDeployment -name dep1 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg -TemplateUri https://raw.githubusercontent.com/gbowerman/azure-myriad/master/vmss-ubuntu-vnet-storage.json

It will ask you any parameters you missed (like location for example).

### Get scale set details

Get-AzureResource -name myvmss -ResourceGroupName myrg -ResourceType Microsoft.Compute/virtualMachineScaleSets -ApiVersion 2015-06-15

or for more detail pipe it through | ConvertTo-Json -Depth 10

or for even more detail add –debug to your command.

###	Scaling out or scaling in

New-AzureResourceGroupDeployment -name dep2 -vmSSName myvmss -instanceCount 2 -ResourceGroupName myrg –TemplateUri https://github.com/gbowerman/azure-myriad/blob/master/vmss-scale-in-or-out.json 

###	Remove a Scale Set

Easy: Remove the resource group:

Remove-AzureResourceGroup -Name myrg

Precise: Remove a resource:

Remove-AzureResource -Name myvmss -ResourceGroupName myrg -ApiVersion 2015-06-15 -ResourceType Microsoft.Compute/virtualMachineScaleSets

## Working with scale sets using CLI

You can deploy VMSS templates and query resources using any current Azure CLI version.
The easiest way to install CLI is from a Docker container. For installing see: <a href="https://azure.microsoft.com/en-us/blog/run-azure-cli-as-a-docker-container-avoid-installation-and-setup/">the azure-cli container announcement</a>.
For using CLI see the: <a href="https://azure.microsoft.com/en-us/documentation/articles/xplat-cli/">Azure CLI documentation</a>

### VM Scale Set CLI examples
### create a resource group
azure group create myrg "Southeast Asia" 

### create a scale set
azure group deployment create -g myrg -n dep2 --template-uri https://raw.githubusercontent.com/gbowerman/azure-myriad/master/vmss-ubuntu-vnet-storage.json

this should ask for parameters dynamically, or you could specify them as arguments

### get scale set details
azure resource show -n vmssname -r Microsoft.Compute/virtualMachineScaleSets -o 2015-06-15 -g myrg
 
### or for more details:
azure resource show –n vmssname –r Microsoft.Compute/virtualMachineScaleSets –o 2015-06-15 –g myrg –json –vv


## Templates 

### vmss-ubuntu-vnet-storage.json

Creates a VNET, storage account, and scale set of identical Ubuntu virtual machines.
InstanceCount parameter describes the number of VMs.

Note: If you want to connect to your VMs from outside the VNET you'll need to also create a public IP address associated with a load balancer or virtualMachine. Hence think of this template as a fragment you can use as part a larger solution rather than a self-contained solution.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-ubuntu-vnet-storage.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-win-vnet-storage.json

Creates a VNET, storage account, and scale set of identical Windows virtual machines.
InstanceCount parameter describes the number of VMs.

Note: If you want to connect to your VMs from outside the VNET you'll need to also create a public IP address associated with a load balancer or virtualMachine. Hence think of this template as a fragment you can use as part a larger solution rather than a self-contained solution.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-win-vnet-storage.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


### vmss-coreos-vnet-storage.json

Creates a VNET, storage account, and scale set of identical CoreOS virtual machines.
InstanceCount parameter describes the number of VMs.

Note: If you want to connect to your VMs from outside the VNET you'll need to also create a public IP address associated with a load balancer or virtualMachine. Hence think of this template as a fragment you can use as part a larger solution rather than a self-contained solution.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-coreos-vnet-storage.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


### mesos-vmss-simple-cluster.json

Create a simple mesos cluster with a single master, with a VM Scale Set of slaves. Connect to port 505 of the public IP address created in your resource group to see the dashboard.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fmesos-vmss-simple-cluster.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


### vmss-scale-in-or-out.json

Reduce or increase the number of VM instances in a Scale Set. Platform independent.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-scale-in-or-out.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


### multiple-vmss-ubuntu-vnet-multiple-storage.json

Create multiple VMSS each with:
A VNET, three storage accounts, and scale set of identical Ubuntu virtual machines.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fmultiple%2Fmultiple-vmss-ubuntu-vnet-multiple-storage-deploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


### vmss-nat-pools.json

Create an Ubuntu VMSS with load balancer, public IP and inbound NAT rules. SSH to port 50000 of the public IP address will connect to port 22 of the 1st VM in the scale set. SSH to port 50001 will connect to port 22 of the second VM and so on.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fnat-pools%2Fvmss-nat-pools.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


### vmss-win-iis-vnet-storage-lb.json

Create a VMSS with load balancer, public IP and Windows VMs with IIS and a basic MVC app configured\installed via the custom script extension.
Port 80 is load balanced to the web app running on each VM Instance.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fnat-pools%2Fvmss-win-iis-vnet-storage-lb.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


### vmss-customimage.json

Create a VMSS from a custom image.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Falanst%2Fazure-myriad%2Fpatch-8%2Fvmss-customimage.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


### autoscale/vmss-win-autoscale.json ###

Deploy a simple Windows based scale set.

How to use:
- Deploy with an instance count of 1.
- RDP into port 50000 and max the CPU.
- After a few minutes additional VMs will be created.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fautoscale%2Fvmss-win-autoscale.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<br/><br/>


### autoscale/vmss-ubuntu-autoscale.json ###

Deploy a simple Linux based scale set.

How to use:
- Deploy with an instance count of 1.
- SSH into port 50000 and max the CPU.
- After a few minutes additional VMs will be created.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fautoscale%2Fvmss-ubuntu-autoscale.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<br/><br/>


### autoscale/vmss-lap-autoscale.json ###

Simple self-contained Ubuntu/Apache/PHP autoscale & load balancing example. Scale Set scales up when avg CPU across all VMs > 60%, scales down when avg CPU < 50%.

- Deploy the scale set with an instance count of 1
- Browse to the website (port 80), which shows the current backend VM name.
- Hit the "Do work" button with an iteration count of say 600.
- After a few minutes the scale set capacity will increase, and refreshing the browser and going to the home page a few times will show additional backend VM name(s).
- You can increase the work by connecting to more backend websites, or decrease by letting the iterations time-out, in which case the scale set will scale down.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fautoscale%2Fvmss-lap-autoscale.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


