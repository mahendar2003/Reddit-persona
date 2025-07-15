 Reddit User Persona Generator

Simple tool to scrape a Reddit user's public activity and create a plain‑text persona summary with OpenAI.

 Quick Start


Add a .env with:

REDDIT_CLIENT_ID=xxx
REDDIT_CLIENT_SECRET=yyy
REDDIT_USER_AGENT=my-app
OPENAI_API_KEY=sk-***


 Note: .env file should be in the same folder a od script.py

bash

1. pip install -r requirements.txt
2. python script.py




test.py is a simple python file to check if the reddit credentials and access are correct in .env file.