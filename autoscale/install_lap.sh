#!/bin/bash
# wait for Linux Diagnostic Extension to complete
while ( ! grep "Start mdsd" /var/log/azure/Microsoft.OSTCExtensions.LinuxDiagnostic/2.1.5/extension.log); do
    sleep 5
done

# install Apache and PHP
apt-get -y update
apt-get -y install apache2 php5

# write some PHP
echo \<\?php \$hostname = gethostname\(\)\; \?\> > /var/www/html/index.php
echo \<center\>\<h1\>Scale Set App - \<\?php echo \"\$hostname\"\;\?\>\</h1\>\</center\> >> /var/www/html/index.php
echo \<br/\>\<br/\>\<br/\> >> /var/www/html/index.php
echo \<\?php phpinfo\(\)\; \?\> >> /var/www/html/index.php
rm /var/www/html/index.html
# restart Apache
apachectl restart

