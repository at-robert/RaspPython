HiMediaMacAddr=DC:9B:9C:94:E9:BC
HiMediaMacIP=$(echo "$password\n" | sudo -S nmap -sP 192.168.0.* | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "$3;}' | grep -i "$HiMediaMacAddr" | sort)
HiMediaMacIP=$(echo "$HiMediaMacIP" | sed 's/=>//g' | sed 's/DC:9B:9C:94:E9:BC//g' | sed 's/^[ \t]*//g' | sed 's/[ \t]*$//g')
echo "IPHONE5S IP = $HiMediaMacIP"
