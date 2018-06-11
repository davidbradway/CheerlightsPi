#!/bin/bash
sudo service cheerlights.sh status| grep 'FAIL\|failed' > /dev/null 2>&1
if [ $? != 0 ]
then
    echo "Still running"
    sudo service cheerlights.sh status
else
    echo "FAILED"
    sudo service cheerlights.sh start
fi
