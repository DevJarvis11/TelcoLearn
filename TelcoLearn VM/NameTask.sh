read -p "Enter your name: " name
echo $name

read -p "Enter your age: " age
echo $age

if [[ $name =~ [a-zA-Z/_]+$ ]] && (( age > 0 && age < 100 )); then
	echo "Correct"
else
	echo "Not Correct"
fi
