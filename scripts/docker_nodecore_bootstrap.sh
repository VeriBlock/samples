#!/usr/bin/env bash

echo "This script will generate a directory, install the latest nodecore bootstrap, and start a docker image which will start nodecore. Make sure you are running this as root!"
read -p "Continue (y/n)?" choice
case "$choice" in 
  y|Y ) echo "yes";;
  n|N ) exit 0;;
  * ) exit 0;;
esac

LATEST_BOOTSTRAP=`curl -s https://explore.veriblock.org/api/stats/download | jq -r .bootstrapfile_zip`
BOOTSTRAP="$(basename $LATEST_BOOTSTRAP)"

echo "Starting script!"
## Shoutout panda
echo "Checking to see if your system meets the minimum requirements for NodeCore to run..."
TOTALMEM=$(cat /proc/meminfo | head -n 1 | tr -d -c 0-9)
TOTALMEM=$(($TOTALMEM/1000000))
echo System Memory: $TOTALMEM GB
TOTALCORES=$(nproc)
echo System Cores: $TOTALCORES
TOTALDISK=$(df -H "$HOME" | awk 'NR==2 { print $2 }' | tr -d -c 0-9)
echo Disk Size: $TOTALDISK GB
FREESPACE=$(df -H "$HOME" | awk 'NR==2 { print $2 }' | tr -d -c 0-9)
echo Free Disk Space: $FREESPACE GB

if [ $TOTALMEM -lt 4 ]
then
    echo "Sorry, but this system needs at least 4GB of RAM for NodeCore to run.  Exiting Install..."
    exit
elif [ $TOTALCORES -lt 2 ]
then
    echo "Sorry, but this system needs at least 2 cores for NodeCore to run.  Exiting Install..."
    exit
elif [ $TOTALDISK -lt 50 ]
then
    echo "Sorry, but this system needs at least 50GB total disk space for NodeCore to run.  Exiting Install..."
    exit
elif [ $FREESPACE -lt 15 ]
then
    echo "Sorry, but this system needs at least 15GB free disk space for NodeCore to run.  Exiting Install..."
    exit
else
    echo "Your system is suitable, continuing installation of NodeCore..."
fi

echo "========================"

docker  > /dev/null 2>&1
if [ $? != 0 ]
then
  echo "Please install Docker!"
  exit 0
  else
  echo "Docker is installed!"
fi

echo "========================="
mkdir -p /root/nc_data/mainnet
echo "/root/_nc_data/mainnet directory created"

echo "========================="
sleep 5
echo "downloading the latest bootstrap"
wget -P /root/nc_data/mainnet $LATEST_BOOTSTRAP

echo "========================="
unzip /root/nc_data/mainnet/$BOOTSTRAP -d /root/nc_data/mainnet/
echo "bootstrap unzipped!"

echo "========================="
echo "rpc.whitelist.addresses=172.17.0.1" > /root/nc_data/nodecore.properties
echo "Added docker0 bridge to nodecore.properties"

echo "========================="
sleep 5
echo "starting docker image"
docker run -d --name scripttest -v /root/nc_data:/data -p 7500:7500 -p 10500:10500 docker.io/veriblock/nodecore 
echo "docker image started"

sleep 5
echo "========================="
docker ps
