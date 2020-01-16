find ~ -maxdepth 1 -mindepth 1 -type d -exec sh -c '(echo {} && cd {} && git fs && echo)' \;
sudo systemctl start mqttclient
