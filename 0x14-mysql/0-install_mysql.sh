#!/bin/bash

# Add MySQL APT repository
wget https://dev.mysql.com/get/mysql-apt-config_0.8.16-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.16-1_all.deb

# Set non-interactive mode for debconf
export DEBIAN_FRONTEND=noninteractive

# Automatically configure MySQL APT repository without prompts
sudo debconf-set-selections <<< "mysql-apt-config mysql-apt-config/select-server select mysql-5.7"
sudo debconf-set-selections <<< "mysql-apt-config mysql-apt-config/select-tools select Enabled"
sudo debconf-set-selections <<< "mysql-apt-config mysql-apt-config/select-preview select Disabled"

# Update package list
sudo apt-get update

# Install MySQL 5.7
sudo apt-get install -y mysql-server=5.7.42-1ubuntu18.04

# Remove the MySQL APT repository configuration file
sudo rm /etc/apt/sources.list.d/mysql.list

# Restart MySQL service
sudo service mysql restart
