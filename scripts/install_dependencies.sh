#!/bin/bash

# Update package list
apt-get update

# Install ODBC drivers
apt-get install -y unixodbc unixodbc-dev

# Clean up
apt-get clean

