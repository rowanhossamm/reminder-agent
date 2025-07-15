from google.adk.agents import Agent

def send_email(contact, subject, body):
    print(f"[Email] To: {contact}, Subject: {subject}, Body: {body}")

mail_agent = Agent(
    name="mail_agent",
    model="gemini-2.0-flash-exp",
    description="Email sender agent",
    instruction="Send emails to contacts",
    tools=[send_email]
)
