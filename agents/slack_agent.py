from google.adk.agents import Agent
from agents.tool_wrapper import Tool

def send_slack_message(contact, message):
    print(f"[Slack] Message to {contact}: {message}")

send_slack_tool = Tool(
    name="send_slack_message",
    description="Send Slack messages",
    func=send_slack_message
)

slack_agent = Agent(
    name="slack_agent",
    model="gemini-2.0-flash-exp",
    description="Slack message sender",
    instruction="Send Slack messages",
    tools=[send_slack_tool]
)
