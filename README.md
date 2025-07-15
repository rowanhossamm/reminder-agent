A hands-on prototype demonstrating Agentic AI using Google’s Agent Development Kit (ADK), simulating how autonomous agents fetch contacts and send notifications via Slack and Email — inspired by enterprise workflows.
Setup Instructions
Uses UV, a fast modern Python package manager.

1. Install UV globally
pip install uv

2. Initialize the project
uv init REMINDER_AGENT
cd REMINDER_AGENT

3. Open in VS Code code .

4. Create virtual environment
uv venv

5. Activate (Windows)
.\.venv\Scripts\activate

6. Install Google ADK
uv add google-adk

API Key Setup
You’ll need API keys for Slack or Gmail integrations.

Create a file named .env
Add your keys:
API_KEY=your_api_key_here

Run the Project
python main.py
