# azure-myriad
Templates for VM Scale Sets. 

Note: VM Scale Sets are announced but not yet in preview:
- They will only work with whitelisted Azure subscriptions.
- API is not yet public and subject to breaking change.

### vmss-vnet-storage-win.json

Creates a VNET, storage account, and scale set of identical Windows virtual machines.
InstanceCount parameter describes the number of VMs.

### vmss-scale-out-win.json

Create a Windows VM Scale Set with an existing storage account and VNET, and change the number of instances. Used for scaling out.
InstanceCount parameter describes the number of VMs.

### vmss-scale-in.json

Reduce the number of VM instances in a Scale Set (scale-in). Platform independent.
InstanceCount parameter describes the number of VMs.
