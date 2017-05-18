HiMediaMacAddr=4C:8D:79:7F:59:F8
HiMediaMacIP=$(echo "$password\n" | sudo -S nmap -sP 192.168.0.* | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "$3;}' | grep -i "$HiMediaMacAddr" | sort)
HiMediaMacIP=$(echo "$HiMediaMacIP" | sed 's/=>//g' | sed 's/4C:8D:79:7F:59:F8//g' | sed 's/^[ \t]*//g' | sed 's/[ \t]*$//g')
echo "IPHONE5 IP = $HiMediaMacIP"
