#!/bin/bash
# $1 = Azure storage account name
# $2 = Azure storage account key
# $3 = Azure file share name
# $4 = mountpoint path

# For more details refer to https://azure.microsoft.com/en-us/documentation/articles/storage-how-to-use-files-linux/

storageaccountname=$1
storageaccountkey=$2
filesharename=$3
mountpointpath=$4

apt-get -y update

# Check for distro use proper command to unstall CIFS Utils
# Check if user is on-cloud or on-prem - Check for SMB 3.0 or 2.1
# Check if storage account and VM are in same region
# Mapping for distro to SMB support mapping
# Check if user is on-prem - Check for encryption support (check for kernel versin > 4.11 or greater Ubintu, SUSE)

sudo apt-get install cifs-utils
mkdir "$mountpointpath"
sudo mount -t cifs //"$storageaccountname".file.core.windows.net/"filesharename" "$mountpointpath" -o vers=3.0,username="$storageaccountname",password="$storageaccountkey",dir_mode=0755,file_mode=0664
[ "$?" == 0 ]  && echo "succeed!" || echo "failed!"

