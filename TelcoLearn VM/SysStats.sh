read -p "Do you need system stats: " t

if [ t==cpu ]; then
	lscpu
elif [ t==memory ]; then
	free -h
elif [ t==disc ]; then
	df -h
elif [ t==network ]; then
	ip -a
else
	echo "Bye Bye"
fi
