echo "Starting DB0204 !!!"
irsend SEND_ONCE HiMEDIA KEY_POWER
sleep 3
irsend SEND_ONCE DB0204 KEY_ENTER
sleep 3
irsend SEND_ONCE DB0204 KEY_DOWN
sleep 1
irsend SEND_ONCE DB0204 KEY_ENTER
sleep 3
irsend SEND_ONCE DB0204 KEY_ENTER
sleep 1
irsend SEND_ONCE DB0204 KEY_DOWN
sleep 1
irsend SEND_ONCE DB0204 KEY_DOWN
sleep 1
irsend SEND_ONCE DB0204 KEY_DOWN
sleep 1
irsend SEND_ONCE DB0204 KEY_ENTER
echo "Waiting for HiMedia !!!"
sleep 40
echo "Starting HiMedia !!!"
irsend SEND_ONCE HiMEDIA KEY_DOWN
sleep 2
irsend SEND_ONCE HiMEDIA KEY_LEFT
sleep 2
irsend SEND_ONCE HiMEDIA KEY_ENTER
sleep 4
irsend SEND_ONCE HiMEDIA KEY_RIGHT
sleep 3
irsend SEND_ONCE HiMEDIA KEY_ENTER
sleep 3
irsend SEND_ONCE HiMEDIA KEY_ENTER
sleep 2
irsend SEND_ONCE HiMEDIA KEY_DOWN
sleep 2
irsend SEND_ONCE HiMEDIA KEY_DOWN
sleep 2
irsend SEND_ONCE HiMEDIA KEY_DOWN
sleep 2
irsend SEND_ONCE HiMEDIA KEY_DOWN
sleep 2
irsend SEND_ONCE HiMEDIA KEY_DOWN
sleep 2
irsend SEND_ONCE HiMEDIA KEY_DOWN
sleep 2
irsend SEND_ONCE HiMEDIA KEY_ENTER
sleep 3
irsend SEND_ONCE HiMEDIA KEY_DOWN
sleep 2
irsend SEND_ONCE HiMEDIA KEY_ENTER
sleep 2
irsend SEND_ONCE HiMEDIA KEY_ENTER
sleep 6
irsend SEND_ONCE HiMEDIA KEY_ENTER
sleep 2
#irsend SEND_ONCE VIZIO_TV KEY_POWER
echo "Hello world by Robert end!!!"
for file in $(find /media/pi/SANDISK/Music/MP3/ -type f -name "*.mp3");
do
	filename=$file
	echo "$filename"
	omxplayer -o local $filename
done
echo "Test songs"
