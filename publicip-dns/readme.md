# Azure VM scale set networking preview page 

The templates and instructions in this repo are for new and recent network features being added to Azure VM scale sets. Some of these features are recently GA, and other are in preview, either limited (your subscription needs to be enabled to use them) or public (anyone can use them).

## Feature status
Last updated: 5/9/2017

| Feature                    | Description                                                             | Status          | Start using |
|----------------------------|-------------------------------------------------------------------------|-----------------|-------------|
| Configurable DNS server    | Define DNS server addresses for your VMSS VM NICs to use                | Limited preview | [Sign-up](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR3nO_Bpm1Q9BkpyqngZiqHFUNkkzNjZBTkJWSktZQVBQTFZNOTNNOEczMi4u)|
| DNS label                  | Include a domain name label with your scale set VM public IP addresses  | Limited preview | Stand-by    |
| Multiple NICs per VM       | Support multiple NICs on each VMSS VM                                   | Limited preview | [Sign-up](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR3nO_Bpm1Q9BkpyqngZiqHFUNkkzNjZBTkJWSktZQVBQTFZNOTNNOEczMi4u)|
| Multiple CA for VMSS       | Multiple Customer Address space per VMSS VM                             | Limited preview | [Sign-up](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR3nO_Bpm1Q9BkpyqngZiqHFUNkkzNjZBTkJWSktZQVBQTFZNOTNNOEczMi4u)|
| NSG for VMSS               | Configure Network Security Group at a VM scale set level                | GA              | See below   |
| Public IPv4 address per VM | Assign a public IP address to each VMSS VM                              | Limited preview | [Sign-up](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR3nO_Bpm1Q9BkpyqngZiqHFUNkkzNjZBTkJWSktZQVBQTFZNOTNNOEczMi4u)|


## Registering
Use [this handy form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR3nO_Bpm1Q9BkpyqngZiqHFUNkkzNjZBTkJWSktZQVBQTFZNOTNNOEczMi4u) to send your Azure subscription ID to the Network/VMSS PM team to enable the limited preview feature flag. Please include the scenarios you wish to test so we can set the required feature flag(s) and share any usage guidelines (like region availability).


## Configurable DNS Settings
For DNS, previously scale sets relied on the specific DNS settings of the VNET and subnet they were created in. With configurable DNS, you can now configure the DNS settings for a scale set directly. The DNS settings will then apply to all VMs in the scale set.

### Creating a scale set with configurable DNS servers
To create a VM scale set with a custom DNS configuration, add a dnsSettings JSON packet to the scale set networkInterfaceConfigurations section. Example:
```
    "dnsSettings":{
        "dnsServers":["10.0.0.6"], ["10.0.0.5"]
    }
```

### Creating a scale set with configurable domain name
To create a VM scale set with a custom DNS name, add a dnsSetting JSON packet to the scale set networkInterfaceConfigurations section. Example:

```
          "networkProfile": {
            "networkInterfaceConfigurations": [
              {
                "name": "nic1",
                "properties": {
                  "primary": "true",
                  "ipConfigurations": [
                    {
                      "name": "ip1",
                      "properties": {
                        "subnet": {
                            "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/virtualNetworks/', variables('vnetName'), '/subnets/subnet1')]"
                        },
                        "publicIPAddressconfiguration": {
                          "name": "publicip",
                          "properties": {
                            "idleTimeoutInMinutes": 10,
                              "dnsSetting": {
                                "domainNameLabel": "[parameters('vmssDnsName')]"
                              }
                          }
                        }
```

## Public IP per VM
In general Azure scale set VMs do not require their own public IP addresses, because rather than each VM directly facing the internet, it is more economical and secure to associate a public IP address to a load balancer or an individual VM (aka a jumpbox) which then routes incoming connections to scale set VMs as needed (e.g. through inbound NAT rules).

However some scenarios do require scale set VMs to have their own public IP addresses. An example of this is gaming, where a console needs to make a direct connection to a cloud VM which is doing game processing (e.g. game physics etc.).


### Creating a scale set with public IP per VM
To create a VM scale set that assigns a public IP address to each VM, make sure the API version of the Microsoft.Compute/virtualMAchineScaleSets resource is 2017-03-30, and add a _publicipaddressconfiguration_ JSON packet to the scale set ipConfigurations section. Example:

```
    "publicipaddressconfiguration": {
        "name": "pub1",
        "properties": {
        "idleTimeoutInMinutes": 15
        }
    }
```
Example template: [azuredeploypip.json](https://github.com/gbowerman/azure-myriad/blob/master/publicip-dns/azuredeploypip.json)


### Querying the public IP address of the VMs in a scale set
Until there is full SDK, command line and portal support, the recommended way to query the public IP addresses assigned to scale set VMs is to use the REST API with version _2017-03-30_. E.g.
```
GET https://management.azure.com/subscriptions/{your sub ID}/resourceGroups/{RG name}/providers/Microsoft.Compute/virtualMachineScaleSets/{VMSS name}/publicipaddresses?api-version=2017-03-30
```
You can do this with the [ARM client](http://blog.davidebbo.com/2015/01/azure-resource-manager-client.html), or use the _get_vmss_public_ips()_ function in the [azurerm](https://pypi.python.org/pypi/azurerm) Python library. Alternatively [send REST calls directly](https://msftstack.wordpress.com/2016/01/03/how-to-call-the-azure-resource-manager-rest-api-from-c/) using authenticated calls with your language of choice, or use Fiddler etc.

Example:
```
GET https://management.azure.com/subscriptions/your-subscription-id/resourceGroups/gbpiptst4/providers/Microsoft.Compute/virtualMachineScaleSets/gbpiptst4/publicipaddresses?api-version=2017-03-30

{
  "value": [
    {
      "name": "pub1",
      "id": "/subscriptions/your-subscription-id/resourceGroups/gbpiptst4/providers/Microsoft.Compute/virtualMachineScaleSets/gbpiptst4/virtualMachines/0/networkInterfaces/gbpiptst4nic/ipConfigurations/gbpiptst4ipconfig/publicIPAddresses/pub1",
      "etag": "W/\"a64060d5-4dea-4379-a11d-b23cd49a3c8d\"",
      "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "ee8cb20f-af8e-4cd6-892f-441ae2bf701f",
        "ipAddress": "13.84.190.11",
        "publicIPAddressVersion": "IPv4",
        "publicIPAllocationMethod": "Dynamic",
        "idleTimeoutInMinutes": 15,
        "ipConfiguration": {
          "id": "/subscriptions/your-subscription-id/resourceGroups/gbpiptst4/providers/Microsoft.Compute/virtualMachineScaleSets/gbpiptst4/virtualMachines/0/networkInterfaces/gbpiptst4nic/ipConfigurations/gbpiptst4ipconfig"
        }
      }
    },
    {
      "name": "pub1",
      "id": "/subscriptions/your-subscription-id/resourceGroups/gbpiptst4/providers/Microsoft.Compute/virtualMachineScaleSets/gbpiptst4/virtualMachines/3/networkInterfaces/gbpiptst4nic/ipConfigurations/gbpiptst4ipconfig/publicIPAddresses/pub1",
      "etag": "W/\"5f6ff30c-a24c-4818-883c-61ebd5f9eee8\"",
      "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "036ce266-403f-41bd-8578-d446d7397c2f",
        "ipAddress": "13.84.159.176",
        "publicIPAddressVersion": "IPv4",
        "publicIPAllocationMethod": "Dynamic",
        "idleTimeoutInMinutes": 15,
        "ipConfiguration": {
          "id": "/subscriptions/your-subscription-id/resourceGroups/gbpiptst4/providers/Microsoft.Compute/virtualMachineScaleSets/gbpiptst4/virtualMachines/3/networkInterfaces/gbpiptst4nic/ipConfigurations/gbpiptst4ipconfig"
        }
      }
    }
```

### Public IP address template examples

Please help us create more template examples by submitting pull requests for your templates to this repo. Thanks!

This [example](https://github.com/gbowerman/azure-myriad/blob/master/publicip-dns/azuredeploypip.json) is a simple self-contained Ubuntu autoscale example which uses Azure Managed Disks. The scale set scales out when avg CPU across all VMs > 60%, and scales in when avg CPU < 30%. With public IP per VM configured, you can access each VM via both inbound NAT rules (using the load balancer public IP address with ports starting at 50000), and directly by going to each VMs public IP address at port 9000.

- Deploy the scale set with an instance count of 1.
- Browse to the website of vm#0 (port 9000), which shows the current backend VM name.
- To start doing work on the first VM browse to dns:9000/do_work.
- After a few minutes the VM Scale Set capacity will increase.
- You can stop doing work by browsing to dns:9000/stop_work.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fpublicip-dns%2Fazuredeploypip.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fpublicip-dns%2Fazuredeploypip.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

## Providing feedback
Please log issues against this repo to provide feedback.