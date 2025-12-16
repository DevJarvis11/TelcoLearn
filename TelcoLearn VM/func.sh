add() {
	read -p "Enter sum1: " num1
	read -p "Enter sum2: " num2
	sum=$(( $num1 + $num2 ))
	echo $sum
}
add
