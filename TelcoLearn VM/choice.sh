read -p "Enter choice: " choice
case $choice in
1) echo "Start Service";;
2) echo "Stop Service";;
3) echo "Status";;
*) echo "Invalid option";;
esac
