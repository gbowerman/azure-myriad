### Large VMSS test templates ###

Templates to test large VM scale sets (101 -> 1000 VMs).

Note 1/27/16: 

The 'md' managed disks templates in this repo won't work for everyone yet as they rely on the Azure Managed Disks feature which is in preview. Managed Disks is going GA very soon though and you'll start to see templates in the Azure Quickstart Templates use them to avoid having to manage lots of storage accounts..

### elastic.json - Up to 1000 VMs, managed disks, Elastic search cluster, Ubuntu 14.04

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fbigtest%2Felastic.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fbigtest%2Felastic.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>


### vmss-ubuntu-md.json - Up to 1000 VMs, managed disks, Ubuntu 16.04


<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fbigtest%2Fvmss-ubuntu-md.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fbigtest%2Fvmss-ubuntu-md.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>


### vmss-ubuntu-md-datadisk.json - Up to 1000 VMs, managed disks, attached data disks, Ubuntu 16.04


<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fbigtest%2Fvmss-ubuntu-md-datadisk.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fbigtest%2Fvmss-ubuntu-md-datadisk.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>


### vmss-app-gateway-unmanaged.json - Up to 1000 VMs, App Gateway, no load balancer, unmanaged disks


<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fbigtest%2Fvmss-app-gateway-unmanaged.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fbigtest%2Fvmss-app-gateway-unmanaged.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>