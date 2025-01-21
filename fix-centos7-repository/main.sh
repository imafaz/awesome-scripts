#!/bin/sh

echo "Backing up current yum.repos.d files..."
mv /etc/yum.repos.d /etc/yum.repos.d.backup

echo "Creating new yum.repos.d directory..."
mkdir /etc/yum.repos.d

echo "Downloading and placing CentOS-Base.repo..."
wget -O /etc/yum.repos.d/CentOS-Base.repo "https://raw.githubusercontent.com/imafaz/awesome-scripts/refs/heads/main/fix-centos7-repository/CentOS-Base.repo"

echo "Repositories successfully replaced."
echo "Now you can use the 'yum' command!"