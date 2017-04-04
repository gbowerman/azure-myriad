## Autoscale demo app on Ubuntu 16.04

Simple self-contained Ubuntu autoscale example. VM Scale Set scales up when avg CPU across all VMs > 60%, scales down when avg CPU < 30%.

- Deploy the scale set with an instance count of 1 
- After it is deployed look at the resource group public IP address resource (in portal or resources explorer). Get the IP or domain name.
- Browse to the website of vm#0 (port 9000), which shows the current backend VM name.
- To start doing work on the first VM browse to dns:9000/do_work
- After a few minutes the VM Scale Set capacity will increase.
- You can stop doing work by browsing to dns:9000/stop_work.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-ubuntu-scale%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-ubuntu-scale%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

### Public IP and DNS testing testing example

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-ubuntu-scale%2Fazuredeploypip.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fvmss-ubuntu-scale%2Fazuredeploypip.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

