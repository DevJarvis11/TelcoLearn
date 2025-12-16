read -p "Enter num1: " num1
read -p "Enter num2: " num2

if [ $num1 -eq $num2 ]; then
	echo "Both Numbers are equal"
else
	echo "Not same"
fi
