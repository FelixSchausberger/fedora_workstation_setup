#!/bin/bash

# Create directory if it doesn't exist
DRIVE_DIR="$HOME/Documents/gDrive"
mkdir -p "${DRIVE_DIR}"

# Mount the gDrive using rclone
rclone --vfs-cache-mode writes mount 'gDrive': "${DRIVE_DIR}"
