import os
import slack

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if 'Hello' in data.get('text', []):
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!, this is a Chrome-Bot running on Linux.",
            thread_ts=thread_ts
        )

@slack.RTMClient.run_on(event='message')
def youtube_event(**payload):
    data = payload['data']

    #Ignore own messages
    if 'subtype' in data and data['subtype'] == 'bot_message':
        return
    
    #print(data)
    web_client = payload['web_client']
    channel_id = data['channel']
    message =  data.get('text', [])
#    print((str(message)).lower())
    thread_ts = data['ts']


    if 'youtube' in (str(message)).lower():
        print('received >> ', message)
        youtube_keyword, youtube_link = message.split()
        print('PERFORMING ACTION - Youtube Redirect >> ', youtube_link)

        web_client.chat_postMessage(
                channel=channel_id,
                text="opening youtube link -- {}".format(youtube_link),
                thread_ts=thread_ts,
                hidden=False
                )

slack_token = "xoxb-942270408645-941809432772-Eow6s1dOzolTcOWCGEEHwUyg"
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
