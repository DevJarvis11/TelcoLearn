for i in {1..10}; do
{
echo "Run #$1"
printf "%-15s %-15s\n" "Interface" "IPv4 Address"
ip -4 -0 addr show | awk '{split($4,a,"/"); printf "%-15s %-15s\n", $2, a[1]}'
echo "------------------------------------------------------"
echo
} > showip4.txt
sleep 5
done
