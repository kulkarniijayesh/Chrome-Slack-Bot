#!/bin/bash

trap cleanup 1 2 3 6

cleanup()
{
	echo 'stopping slack bot'
	kill -9 $slackBotPid

	echo 'Stopping api server'
	kill -9 $nodePid

	echo 'Stopping chrome session'
	kill -9 $chromePid
	echo '>> Exiting.'
	exit 1
}

echo 'Starting Chrome-Bot ...'
echo '>> Creating a new chrome session'
echo 'using debugging port 9222'
google-chrome --remote-debugging-port=9222 2> /dev/null &
chromePid="$(echo $!)"
#echo $chromePid
sleep 10
echo '>> Starting api server'
node server.js &
nodePid="$(echo $!)"
#echo $nodePid

echo '>> Starting slack bot'
python ./lib/slack-bot-2.py &
slackBotPid="$(echo $!)"
echo $slackBotPid


while :
do
	sleep 100
done


