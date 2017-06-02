# Azure VM scale set automatic upgrades

Welcome to the VM scale set automatic OS image update preview page. Last update: 5/23/17

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
    "automaticOSUpgrade": "true" or "false",
	"rollingUpgradePolicy": {
		"batchInstancePercent": 20,
		"maxUnhealthyUpgradedInstanceCount": 0,
		"pauseTimeBetweenBatches": "PT0S"
	}
}
```
### Property descriptions
__batchInstancePercent__ – 
The maximum percentage of virtual machine instances in the virtual machine scale set that will be upgraded simultaneously by the rolling upgrade in one batch.
The default value is 20.


__pauseTimeBetweenBatches__ – 
The wait time between completing the update for all virtual machines in one batch and starting the next batch. 
The time duration should be specified in ISO 8601 format for duration (https://en.wikipedia.org/wiki/ISO_8601#Durations)
The default value is 0 seconds (PT0S).

__maxUnhealthyUpgradedInstanceCount__ -         
The maximum number of virtual machine instances which can fail to be successfully upgraded before the Rolling Upgrade is stopped.
This check will happen per batch after each batch is upgraded.
If the number of instances which have failed to be upgraded in this rolling upgrade exceeds this number, the rolling update aborts. The default value is 0.


CRP API version is 2017-03-30

## Example templates

### Automatic rolling upgrades - Ubuntu 16.04-LTS
<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fpreview%2Fupgrade%2Fautoupdate.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Automatic rolling upgrades - Ubuntu 16.04-DAILY-LTS for testing
<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fpreview%2Fupgrade%2Fdailyupdate.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Manual rolling upgrades

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fpreview%2Fupgrade%2Fmanualupdate.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


