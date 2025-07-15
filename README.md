 Reddit User Persona Generator

Simple tool to scrape a Reddit user's public activity and create a plain‑text persona summary with OpenAI.

 Quick Start


Add a .env file with these 4:

REDDIT_CLIENT_ID=xxx

REDDIT_CLIENT_SECRET=yyy

REDDIT_USER_AGENT=my-app

OPENAI_API_KEY=sk-***

Add the correct credentials of reddit client id, client secret and openai key from their official website.
Reddit user agent can be any name eg. persona-scrapper

 Note: .env file should be in the same folder a od script.py

bash

1. pip install -r requirements.txt

2. python script.py




test.py is a simple python file to check if the reddit credentials and access are correct in .env file.
