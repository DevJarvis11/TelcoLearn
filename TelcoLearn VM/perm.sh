read -p "Enter file: " file
if [ -x $file ]; then
	echo "File has perm"
else
	echo "No perm"
fi
