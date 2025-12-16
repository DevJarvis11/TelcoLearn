#!/bin/bash

echo "Choose an option:"
echo "1) Create File"
echo "2) Delete File"
echo "3) Copy File"
read -p "Enter your choice (1/2/3): " choice

case $choice in

1)
    read -p "Enter the filename to create: " filename
    touch "$filename"
    echo "File '$filename' created successfully."
    ;;

2)
    read -p "Enter the filename to delete: " filename
    if [ -f "$filename" ]; then
        rm "$filename"
        echo "File '$filename' deleted."
    else
        echo "File not found!"
    fi
    ;;

3)
    read -p "Enter source file: " src
    read -p "Enter destination file: " dest
    if [ -f "$src" ]; then
        cp "$src" "$dest"
        echo "File copied from '$src' to '$dest'."
    else
        echo "Source file not found!"
    fi
    ;;

*)
    echo "Invalid option"
    ;;
esac
