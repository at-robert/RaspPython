HiMediaMacAddr=B8:27:EB:E0:38:F9
HiMediaMacIP=$(echo "$password\n" | sudo -S nmap -sP 192.168.0.* | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "$3;}' | grep -i "$HiMediaMacAddr" | sort)
HiMediaMacIP=$(echo "$HiMediaMacIP" | sed 's/=>//g' | sed 's/B8:27:EB:E0:38:F9//g' | sed 's/^[ \t]*//g' | sed 's/[ \t]*$//g')
echo "RaspX IP = $HiMediaMacIP"

sudo ssh pi@$HiMediaMacIP "sudo shutdown -h now"

echo "Stoping HiMedia !!!"
irsend SEND_ONCE HiMEDIA KEY_POWER
sleep 3
irsend SEND_ONCE DB0204 KEY_POWER
sleep 3
irsend SEND_ONCE VIZIO_TV KEY_POWER
sleep 3
echo "All devices are power down now!!!"
sudo shutdown -h now
