# Deploy scale set to existing VNET example

Simple example to show how to deploy a new VM Scale Set to an existing VNET. If you already have a VNET and know the VNET and subnet name, you can skip the create-vnet.json template and deploy the create-vmss.json one directly.

Note: Make sure you're using the same resource group that your VNET is in.

### Create VNET
<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fexisting-vnet%2Fcreate-vnet.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Create VMSS

Use the VNET and subnet name you specified when creating the VNET as parameters. This templates creates all the other components of a scale set, like storage accounts etc.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fexisting-vnet%2Fcreate-vmss.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

