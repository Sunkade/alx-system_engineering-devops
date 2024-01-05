#!/usr/bin/env bash
# 0-install_mysql.sh

# Update the package list
sudo apt-get update

# Install MySQL Server 5.7
sudo apt-get install -y mysql-server-5.7

# Output the MySQL version to verify installation
mysql --version
