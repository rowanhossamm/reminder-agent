from google.adk.agents import Agent
from tools.get_contacts import get_contacts
from agents.slack_agent import slack_agent
from agents.mail_agent import mail_agent

def send_all_messages():
    contacts = get_contacts()
    for contact in contacts:
        slack_agent.tools[0](contact, "Hi from ADK web!")
        mail_agent.tools[0](contact, "Reminder", "Don’t forget our meeting today.")
    return f"✅ Messages sent to {len(contacts)} contacts."

root_agent = Agent(
    name="messages_agent",
    model="gemini-2.0-flash-exp",
    description="Sends messages through Slack and Email",
    instruction="When I say things like 'send reminder', 'notify everyone', or 'send message to all', use Slack and Email to notify all contacts using the send_all_messages tool.",
    tools=[send_all_messages]
)
