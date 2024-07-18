from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="xoxb-your-slack-bot-token")

try:
    response = client.chat_postMessage(channel='#random', text="Hello, World!")
except SlackApiError as e:
    print(f"Error: {e.response['error']}")