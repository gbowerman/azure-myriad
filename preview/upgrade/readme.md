# Azure VM scale set automatic upgrades

Welcome to the VM scale set automatic OS image update preview page. Last update: 5/19/17

Note: Automatic OS upgrades are being previewed only for non-Service Fabric scale sets for now. Adding support for Service Fabric is work in progress.

## Pre-requisites
Automatic OS upgrades are offered when the following conditions are met:

	The OS image is a platform Image only with Version = _latest_.
    
    The following SKUs during the intial preview (more will be added):
	
		Publisher: MicrosoftWindowsServer
		Offer: WindowsServer
		Sku: 2012-R2-Datacenter
		Version: latest
		
		Publisher: Canonical
		Offer: UbuntuServer
		Sku: 16.04-LTS
		Version: latest

## How to configure auto-updates

- Sign up for the limited preview (details will be provided)

- Upgrade policy is set to Rolling. 

- Syntax
```
"upgradePolicy": {
    "mode": "Rolling",
    "automaticOSUpgrade": "true" or "false"
}
```

CRP API version is 2017-03-30

## Example templates

### Automatic rolling upgrades

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fpreview%2Fupgrade%2Fautoupdate.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fpreview%2Fupgrade%2Fautoupdate.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

### Manual rolling upgrades

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fpreview%2Fupgrade%2Fmanualupdate.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fpreview%2Fupgrade%2Fmanualupdate.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

