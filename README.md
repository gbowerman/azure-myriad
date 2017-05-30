# azure-myriad - templates for Azure virtual machine scale sets

## Do not use these templates - they may not be up to date

This repo is for experimental templates which are not maintained. Therefore there is no guarantee they will still be working, or be using the latest recommendations if you try and use them.

If you're looking for supported templates for VM Scale Sets go here: <a href="https://github.com/Azure/azure-quickstart-templates">https://github.com/Azure/azure-quickstart-templates</a>

If you are looking for templates specifically for Azure Managed disks and can't find the one you're looking for in Quickstart templates, try [https://github.com/chagarw/MDPP](https://github.com/chagarw/MDPP).


[VM Scale Sets](https://azure.microsoft.com/services/virtual-machine-scale-sets/) allow you to deploy and manage a group of identical virtual machines as a set. Advantages include:
-	Autoscale - simply change the instance count and Scale Sets will increase or decrease the number of VMs evenly across update and fault domains.
-	Performance - deploying multiple VMs results in a single call to the fabric, allowing inherent performance optimizations.
-	Customization - built on Azure IaaS, Scale Sets support all Windows and Linux VMs including custom images and extensions.
-	Ease of management - building on the simple declarative modelling introduced with Azure Resource Manager, Scale Sets are the simplest way to manage sets of identical VMs. Focus on compute at scale without managing scaling of storage accounts and NICs.


### Limitations

Please note the following limitations:

-	For custom images you can only have a single storage account and are hence limited to 20 VMs in a scale set (or 40 if you set the overprovision property to "false". This limitation is being removed soon, and there is a preview currently underway for managed disks which fixes it.
-	Maximum number of platform image VMs in a scale set is 100. This will be increased in the future, and there is a preview currently underway for larger scale sets.

## Working with scale sets using PowerShell

See: [Create a Windows Virtual Machine Scale Set using Azure PowerShell](https://azure.microsoft.com/en-us/documentation/articles/virtual-machine-scale-sets-windows-create/), or just install the latest Azure PowerShell and run: 

&nbsp;&nbsp;&nbsp;_gcm \*vmss\*_

###	Scaling out or scaling in

See [Change the instance count of an Azure VM Scale Set](https://msftstack.wordpress.com/2016/05/13/change-the-instance-count-of-an-azure-vm-scale-set/)


## Working with scale sets using CLI

tl;dr Install the latest Azure CLI and run:

&nbsp;&nbsp;&nbsp;azure vmss -h

&nbsp;&nbsp;&nbsp;azure vmssvm -h

See [Create a Linux Virtual Mache Scale Set using Azure CLI](https://azure.microsoft.com/documentation/articles/virtual-machine-scale-sets-linux-create-cli/)


## Templates 

Note: Some of these are experimental and some are not maintained. The official repository for VM Scale Set example templates is: [Azure Quick Start Templates](https://github.com/Azure/azure-quickstart-templates)

### vmss-ubuntu-vnet-storage.json

Creates a VNET, storage account, and scale set of identical Ubuntu virtual machines.
InstanceCount parameter describes the number of VMs.

Note: If you want to connect to your VMs from outside the VNET you'll need to also create a public IP address associated with a load balancer or virtual machine. Hence think of this template as a fragment you can use as part a larger solution rather than a self-contained solution.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-ubuntu-vnet-storage.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

Here's a similar template which authenticates with a public key instead of a password..

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-sshkey-ubuntu.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-win-vnet-storage.json

Creates a VNET, storage account, and scale set of identical Windows virtual machines.
InstanceCount parameter describes the number of VMs.

Note: If you want to connect to your VMs from outside the VNET you'll need to also create a public IP address associated with a load balancer or virtual machine. Hence think of this template as a fragment you can use as part a larger solution rather than a self-contained solution.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-win-vnet-storage.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


### vmss-coreos-vnet-storage.json

Creates a VNET, storage account, and scale set of identical CoreOS virtual machines.
InstanceCount parameter describes the number of VMs.

Note: If you want to connect to your VMs from outside the VNET you'll need to also create a public IP address associated with a load balancer or virtual machine. Hence think of this template as a fragment you can use as part a larger solution rather than a self-contained solution.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-coreos-vnet-storage.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


### vmss-scale-in-or-out.json

Reduce or increase the number of VM instances in a Scale Set. Platform independent. Note: Check the sku setting in the template and make sure it matches the virtual machine size in your existing VM Scale Set.
InstanceCount parameter describes the number of VMs.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-scale-in-or-out.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


### vmss-linux-customimage.json

Create a VMSS from a custom image.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-linux-customimage.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### vmss-minecraft-custom.json

Create a VMSS from a custom Minecraft server image, including a load balancer rule to route incoming Minecraft default TCP port connections to 25565.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-minecraft-custom.json" target="_blank">
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
- After it is deployed look at the resource group public IP address resource (in portal or resources explorer). Get the IP or domain name.
- Browse to the website (port 80), which shows the current backend VM name.
- Hit the "Do work" button with an iteration count of say 300 (represents seconds of max CPU).
- After a few minutes the scale set capacity will increase, and refreshing the browser and going to the home page a few times will show additional backend VM name(s).
- You can increase the work by connecting to more backend websites, or decrease by letting the iterations time-out, in which case the scale set will scale down – hence after about 10 minutes the capacity should be back down to 1.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fautoscale%2Fvmss-lap-autoscale.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Autoscale demo app on Ubuntu 16.04 ###

Simple self-contained Ubuntu autoscale example. VM Scale Set scales up when avg CPU across all VMs > 60%, scales down when avg CPU < 30%.

- Deploy the scale set with an instance count of 1 
- After it is deployed look at the resource group public IP address resource (in portal or resources explorer). Get the IP or domain name.
- Browse to the website (port 9000), which shows the current backend VM name.
- To start doing work on the first VM browse to dns:9000/do_work
- After a few minutes the VM Scale Set capacity will increase.
- You can stop doing work by browsing to dns:9000/stop_work.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-ubuntu-scale%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-ubuntu-scale%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

