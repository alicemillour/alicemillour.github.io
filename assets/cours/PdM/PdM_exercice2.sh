mkdir ~/Downloads/env
cd ~/Downloads/env
cp /etc/environment .
ls
echo -n "Mon ordinateur a tant de processeurs :"
ls /dev/cpu | grep -E "[0-9]+" | wc -l 
ls /dev/cpu | grep -E "[0-9]+" | wc -l > nb_process.txt

