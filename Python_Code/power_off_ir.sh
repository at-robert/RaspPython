echo "Stoping HiMedia !!!"
irsend SEND_ONCE HiMEDIA KEY_POWER
sleep 3
irsend SEND_ONCE DB0204 KEY_POWER
sleep 3
irsend SEND_ONCE VIZIO_TV KEY_POWER
sleep 3
echo "Hello world by Robert end!!!"
sudo shutdown -h now