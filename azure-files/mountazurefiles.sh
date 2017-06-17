

#!/bin/bash
# $1 = Azure storage account name
# $2 = Azure storage account key
# $3 = Azure file share name
# $4 = mountpoint path

# For more details refer to https://azure.microsoft.com/en-us/documentation/articles/storage-how-to-use-files-linux/

apt-get -y update

# Check for distro use proper command to unstall CIFS Utils
# Check if user is on-cloud or on-prem - Check for SMB 3.0 or 2.1
# Check if storage account and VM are in same region
# Mapping for distro to SMB support mapping
# Check if user is on-prem - Check for encryption support (check for kernel versin > 4.11 or greater Ubintu, SUSE)

apt-get install cifs-utils
mkdir $4
mount -t cifs //$1.file.core.windows.net/$3 $4 -o vers=3.0,username=$1,password=$2,dir_mode=0755,file_mode=0664

#Creating a dummy marker files for testing
echo "hello from $HOSTNAME" > $4/$HOSTNAME.txt                                                                         

#logging output
cat  $4/$HOSTNAME.txt 
ls $4


