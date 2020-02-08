# Chrome-Slack-Bot
This is a slack bot to interact with chrome instance running on a remote linux server.

Chrome provides a websockets connection to its DevTools and this socket connection is used to 
run simple commands on chrome.

Current problem statement for which development is in progress:
A linux box can be connected to a display and it would be awesome to play youtube videos on chrome browser of this linux box. And this would in-turn require some basic interaction with videos as well like play, pause, move to next video etc.

Pre-requisites:
1. Install google-chrome, pip, python3, pip
2. Create a new slack bot and get token for this bot

Installation Steps:
1. git clone https://github.com/kulkarniijayesh/Chrome-Slack-Bot.git
2. cd Chrome-Slack-Bot && npm install
3. python3 -m venv env 
4. source ./env/bin/activate
5. pip install -r ./lib/requirements.txt
6. export SLACK_TOKEN=<add your slack bot token here>
7. ./run-chrome-bot.sh
This will start running script run-chrome-bot which will inturn create a new chrome session and a node js server to interact with chrome devtools.

Work-in-progress: branch - dev1.0
