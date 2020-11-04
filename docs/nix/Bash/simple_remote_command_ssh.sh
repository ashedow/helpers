#!/bin/bash
for ip_addr in $(cat ipaddress.txt); do
ssh -t -t ${ip_addr} "bash -s" < /uploadscript.txt
done
#
#more /uploadscript.txt
sudo echo xy12ls1 | passwd --stdin martin