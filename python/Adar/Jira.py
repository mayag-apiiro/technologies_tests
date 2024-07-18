from jira import JIRA

jira = JIRA(server="https://your-domain.atlassian.net", basic_auth=("email@example.com", "api_token"))

issue = jira.issue('PROJ-1')
print(issue.fields.summary)