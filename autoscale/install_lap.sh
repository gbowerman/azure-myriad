#!/bin/bash

while ps aux | grep -v grep | grep "apt-get" > /dev/null; do
    sleep 2
done

apt-get -y update

# install Apache and PHP

while ps aux | grep -v grep | grep "apt-get" > /dev/null; do
    sleep 2
done
apt-get -y install apache2 php5

# write some PHP
\<\?php \$hostname = gethostname\(\)\; \?\> > /var/www/html/index.php
\<center\>\<h1\>Scale Set App - \<\?php echo \"\$hostname\"\;\?\>\</h1\>\</center\> >> /var/www/html/index.php
\<br/\>\<br/\>\<br/\> >> /var/www/html/index.php
\<\?php phpinfo\(\)\; \?\> >> /var/www/html/index.php

# restart Apache
apachectl restart

