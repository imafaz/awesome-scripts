#!/bin/sh

if [ -z "$1" ]; then
  echo "Please provide a proxy, exmple: http://username:password@ip:port/"
  exit 1
fi

PROXY=$1

export http_proxy=$PROXY
export https_proxy=$PROXY
export ftp_proxy=$PROXY
export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"

echo "Proxies have been successfully set."
