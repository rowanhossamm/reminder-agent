import os
from dotenv import load_dotenv
from agents.messages_agent import root_agent

load_dotenv()

if __name__ == "__main__":
    for tool in root_agent.tools:
        tool()
