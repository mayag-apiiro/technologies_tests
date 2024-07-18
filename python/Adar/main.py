# Importing necessary libraries
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from jira import JIRA
from airtable import Airtable

# Initialize Slack client
slack_token = "xoxb-your-slack-bot-token"
slack_client = WebClient(token=slack_token)

# Initialize JIRA client
jira_server = "https://your-domain.atlassian.net"
jira_user = "your-email@example.com"
jira_token = "your-jira-api-token"
jira_client = JIRA(server=jira_server, basic_auth=(jira_user, jira_token))

# Initialize Airtable client
airtable_base_id = 'your_base_id'
airtable_table_name = 'your_table_name'
airtable_api_key = 'your_airtable_api_key'
airtable_client = Airtable(airtable_base_id, airtable_table_name, airtable_api_key)

# Function to post a message to a Slack channel
def post_message_to_slack(channel, message):
    try:
        response = slack_client.chat_postMessage(
            channel=channel,
            text=message
        )
        print(f"Message posted successfully: {response['message']['text']}")
    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")

# Function to create a JIRA issue
def create_jira_issue(project_key, summary, description, issue_type="Task"):
    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': issue_type},
    }
    try:
        new_issue = jira_client.create_issue(fields=issue_dict)
        print(f"Issue created successfully: {new_issue.key}")
    except Exception as e:
        print(f"Error creating JIRA issue: {e}")

# Function to add a record to Airtable
def add_record_to_airtable(fields):
    try:
        record = airtable_client.insert(fields)
        print(f"Record added successfully: {record['id']}")
    except Exception as e:
        print(f"Error adding record to Airtable: {e}")

# Example usage
if __name__ == "__main__":
    slack_channel = "#general"
    slack_message = "Hello, Slack!"
    post_message_to_slack(slack_channel, slack_message)

    jira_project = "TEST"
    jira_summary = "Test Issue"
    jira_description = "This is a test issue created via the JIRA API"
    create_jira_issue(jira_project, jira_summary, jira_description)

    airtable_fields = {
        'Name': 'Test Record',
        'Notes': 'This is a test record added via the Airtable API'
    }
    add_record_to_airtable(airtable_fields)
