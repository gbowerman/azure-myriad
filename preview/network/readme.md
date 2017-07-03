# Azure VM scale set networking preview page 

The templates and instructions in this repo are for new and recent network features being added to Azure VM scale sets. 

## Feature status
Last updated: 07/03/2017 - public preview.

| Feature                    | Description                                                             | Status          | Start using |
|----------------------------|-------------------------------------------------------------------------|-----------------|-------------|
| Accelerated networking - Windows | Accelerated networking enables single root I/O virtualization (SR-IOV) to a VM, greatly improving its networking performance | Public preview | See below |
| Accelerated networking - Linux | Accelerated networking enables single root I/O virtualization (SR-IOV) to a VM, greatly improving its networking performance | Public preview | See below |
| Configurable DNS server    | Define DNS server addresses for your VMSS VM NICs to use                | Public preview | See below|
| DNS label                  | Include a domain name label with your scale set VM public IP addresses  | Public preview | See below |
| Multiple NICs per VM       | Support multiple NICs on each VMSS VM                                   | Public preview | See below|
| Multiple IPs per VM for VMSS       | Multiple Customer Address space per VMSS VM                     | Public preview | See below|
| NSG for VMSS               | Configure Network Security Group at a VM scale set level                | GA              | See below   |
| IPv6 support with Load Balancer | Support private IPv6 addresses on VMSS VM NICs and routing via load balancer pools | See below|
| Public IPv4 address per VM | Assign a public IP address to each VMSS VM                              | pUBLIC preview | See below|


## Registering
These features are in public preview and available to use without registering.

## Accelerated Networking
To use accelerated networking, set enableAcceleratedNetworking to _true_ in your scale set's networkInterfaceConfigurations settings. E.g.
```
"networkProfile": {
    "networkInterfaceConfigurations": [
    {
        "name": "niconfig1",
        "properties": {
        "primary": true,
        "enableAcceleratedNetworking" : true,
        "ipConfigurations": [
                ]
            }
            }
        ]
        }
    }
    ]
}
```

## Configurable DNS Settings
For DNS, previously scale sets relied on the specific DNS settings of the VNET and subnet they were created in. With configurable DNS, you can now configure the DNS settings for a scale set directly. The DNS settings will then apply to all VMs in the scale set.

### Creating a scale set with configurable DNS servers
To create a VM scale set with a custom DNS configuration, add a dnsSettings JSON packet to the scale set networkInterfaceConfigurations section. Example:
```
    "dnsSettings":{
        "dnsServers":["10.0.0.6", "10.0.0.5"]
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
                              "dnsSettings": {
                                "domainNameLabel": "[parameters('vmssDnsName')]"
                              }
                          }
                        }
```

The output, in terms of individual VM dns name would look like: 
```
<vmname><vmindex>.<specifiedVmssDomainNameLabel>
```

## IPv6 support for private IPs and Load Balancer pools
To use IPv6, create an IPv6 public address. E.g.
```
{
    "apiVersion": "2016-03-30",
    "type": "Microsoft.Network/publicIPAddresses",
    "name": "[parameters('ipv6PublicIPAddressName')]",
    "location": "[parameters('location')]",
    "properties": {
        "publicIPAddressVersion": "IPv6",
        "publicIPAllocationMethod": "Dynamic",
        "dnsSettings": {
            "domainNameLabel": "[parameters('dnsNameforIPv6LbIP')]"
        }
    }
}
```
Create your load balancer front end IP Configurations for IPv4, IPv6 as needed

```
"frontendIPConfigurations": [
    {
        "name": "LoadBalancerFrontEndIPv6",
        "properties": {
            "publicIPAddress": {
                "id": "[resourceId('Microsoft.Network/publicIPAddresses',parameters('ipv6PublicIPAddressName'))]"
            }
        }
    }
]
```
Define backend pools as needed..
```
"backendAddressPools": [
    {
        "name": "BackendPoolIPv4"
    },
    {
        "name": "BackendPoolIPv6"
    }
]
```
Define load balancer rules..
```
{
    "name": "LBRuleIPv6-46000",
    "properties": {
        "frontendIPConfiguration": {
            "id": "[variables('ipv6FrontEndIPConfigID')]"
        },
        "backendAddressPool": {
            "id": "[variables('ipv6LbBackendPoolID')]"
        },
        "protocol": "tcp",
        "frontendPort": 46000,
        "backendPort": 60001,
        "probe": {
            "id": "[variables('ipv4ipv6lbProbeID')]"
        }
    }
}
```
Reference the IPv6 pool in the VMSS IPConfigurations..
```
{
    "name": "ipv6IPConfig",
    "properties": {
        "privateIPAddressVersion": "IPv6",
        "loadBalancerBackendAddressPools": [
            {
                "id": "[variables('ipv6LbBackendPoolID')]"
            }
        ]
    }
}
```
Notes:

1.	VMSS Network Profile -> NetworkInterfaceConfiguration supports 2 networkInterfaceIPConfigurations (one for IPv4, one for IPv6)
2.	The networkInterfaceIPConfiguration has an enum – privateIPAddressVersion = IPv4 or IPv6 – in order to identify which one is ipv4 and which one is ipv6
When we say, ipv6 ipconfiguration that means an ipconfiguration with privateIPAddressVersion = IPv6.
3.	Subnet on IPv6 ipconfiguration is null (we don’t support CA’s yet). Other validations apply too (such as counts).
4.	VMSS API version at least 2017-03-30
5.	Load Balancer needs to have IPv4 +  IPv6 configuration – 2 public IP’s (distinguished by publicIPAddressVersion = IPv4|IPv6), 2 backend address pools, lb rules etc. IPv4 nic ipconfig refers to ipv4 load balancer backend pools and IPv6 refers to ipv6 pools.

## Public IPv4 per VM
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
Example template: [azuredeploypip.json](https://github.com/gbowerman/azure-myriad/blob/master/preview/network/azuredeploypip.json)


### Querying the public IP address of the VMs in a scale set
Until there is full SDK, command line and portal support, the recommended way to query the public IP addresses assigned to scale set VMs is to use the [Azure Resource Explorer](https://resources.azure.com), or the REST API with version _2017-03-30_.

To view public IP addresses for a scale set using the Resource Explorer, look at the _publicipaddresses_ section under your scale set. E.g.:
https://resources.azure.com/subscriptions/_your_sub_id_/resourceGroups/_your_rg_/providers/Microsoft.Compute/virtualMachineScaleSets/_your_vmss_/publicipaddresses

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

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fpreview%2Fnetwork%2Fazuredeploypip.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fpreview%2Fnetwork%2Fazuredeploypip.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

## Multiple IP addresses per NIC
You can have up to 50 public IP addresses per NIC.

## Multiple NICs per VM
You can have up to 8 NICs per VM depending on VM size. The following is an example scale set networkProfile showing multiple nic entries (also showing multiple public IP per VM):
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
                "publicipaddressconfiguration": {
                    "name": "pub1",
                    "properties": {
                    "idleTimeoutInMinutes": 15
                    }
                },
                "loadBalancerInboundNatPools": [
                    {
                    "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/loadBalancers/', variables('lbName'), '/inboundNatPools/natPool1')]"
                    }
                ],
                "loadBalancerBackendAddressPools": [
                    {
                    "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/loadBalancers/', variables('lbName'), '/backendAddressPools/addressPool1')]"
                    }
                ]
                }
            }
            ]
        }
        },
        {
        "name": "nic2",
        "properties": {
            "primary": "false",
            "ipConfigurations": [
            {
                "name": "ip1",
                "properties": {
                "subnet": {
                    "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/virtualNetworks/', variables('vnetName'), '/subnets/subnet1')]"
                },
                "publicipaddressconfiguration": {
                    "name": "pub1",
                    "properties": {
                    "idleTimeoutInMinutes": 15
                    }
                },
                "loadBalancerInboundNatPools": [
                    {
                    "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/loadBalancers/', variables('lbName'), '/inboundNatPools/natPool1')]"
                    }
                ],
                "loadBalancerBackendAddressPools": [
                    {
                    "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/loadBalancers/', variables('lbName'), '/backendAddressPools/addressPool1')]"
                    }
                ]
                }
            }
            ]
        }
        }
    ]
}
```

## NSG for VMSS
Network Security Groups can now be applied directly to a VM scale set in the network interface configuration.

Example: 
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
                            }
                "loadBalancerInboundNatPools": [
                                {
                                    "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/loadBalancers/', variables('lbName'), '/inboundNatPools/natPool1')]"
                                }
                            ],
                            "loadBalancerBackendAddressPools": [
                                {
                                    "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/loadBalancers/', variables('lbName'), '/backendAddressPools/addressPool1')]"
                                }
                            ]
                        }
                    }
                ],
                "networkSecurityGroup": {
                    "id": "[concat('/subscriptions/', subscription().subscriptionId,'/resourceGroups/', resourceGroup().name, '/providers/Microsoft.Network/networkSecurityGroups/', variables('nsgName'))]"
                }
            }
        }
    ]
}
```

## Providing feedback
Please log issues against this repo to provide feedback.
