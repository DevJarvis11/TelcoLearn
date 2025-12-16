read -p "Enter Choice: " choice
case $choice in
1) echo "This is new file" >> Ntext.txt ;;
2) read -p "Creating new Dir" NewDir mkdir NewDir;;
3) ls;;
*) echo "Invalid" ;;
esac
