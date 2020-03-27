import requests
import json

wekbook_url = '<SlackIncomingWebhookURL>'

data = {
   'text': 'Hi, I am a test message!',
    'username': 'Mr. Robot',
   'icon_emoji': ':robot_face:'
}

response = requests.post(wekbook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
