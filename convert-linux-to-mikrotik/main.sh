#!/bin/bash -e

if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
elif [ -f /etc/centos-release ]; then
    OS="centos"
else
    echo "This OS is not supported!"
    exit 1
fi

if [[ "$OS" == "ubuntu" || "$OS" == "debian" ]]; then
    apt update -y || exit 1
    apt install wget zip -y || exit 1
elif [[ "$OS" == "centos" || "$OS" == "almalinux" || "$OS" == "rocky" ]]; then
    yum install wget zip -y || exit 1
else
    echo "This OS is not supported!"
    exit 1
fi

wget -4 https://download.mikrotik.com/routeros/7.17/chr-7.17.img.zip -O chr.img.zip || exit 1
gunzip -c chr.img.zip > chr.img || exit 1
STORAGE=$(lsblk | grep disk | cut -d ' ' -f 1 | head -n 1) || exit 1
echo "Selected disk: $STORAGE"
ETH=$(ip route show default | sed -n 's/.* dev \([^\ ]*\) .*/\1/p') || exit 1
echo "Network interface in use: $ETH"
ADDRESS=$(ip addr show $ETH | grep global | cut -d' ' -f 6 | head -n 1) || exit 1
echo "Assigned IP: $ADDRESS"
GATEWAY=$(ip route list | grep default | cut -d' ' -f 3) || exit 1
echo "Gateway address: $GATEWAY"
echo "In the next 10 seconds, all server information will be deleted and MikroTik will be installed. If the information displayed is not correct, stop the process with the CTRL+C command and report the problem on Telegram @mrafaz"
sleep 10
dd if=chr.img of=/dev/$STORAGE bs=4M oflag=sync || exit 1
echo "Process completed. Initiating system reboot..."
echo 1 > /proc/sys/kernel/sysrq || exit 1
echo b > /proc/sysrq-trigger || exit 1