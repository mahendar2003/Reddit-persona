import os
from urllib.parse import urlparse
from pathlib import Path
from dotenv import load_dotenv
import praw
import openai


def load_credentials():
    load_dotenv()
    return {
        "reddit_client_id": os.getenv("REDDIT_CLIENT_ID"),
        "reddit_client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
        "reddit_user_agent": os.getenv("REDDIT_USER_AGENT"),
        "openai_api_key": os.getenv("OPENAI_API_KEY")
    }


def get_reddit_client(creds):
    return praw.Reddit(
        client_id=creds["reddit_client_id"],
        client_secret=creds["reddit_client_secret"],
        user_agent=creds["reddit_user_agent"]
    )


def extract_username(url):
    parsed = urlparse(url)
    parts = parsed.path.strip('/').split('/')
    if 'user' in parts:
        return parts[parts.index('user') + 1]
    return parts[-1]


def scrape_user_content(reddit, username, limit=30):
    user = reddit.redditor(username)
    posts, comments = [], []
    for post in user.submissions.new(limit=limit):
        posts.append(f"Title: {post.title}\nBody: {post.selftext}")
    for com in user.comments.new(limit=limit):
        comments.append(f"Comment: {com.body}")
    return posts, comments


def build_prompt(posts, comments):
    raw = "\n\n".join(posts + comments)
    return (
        "You're analyzing a Reddit user's public activity.\n"
        "Based on their posts and comments below, \n"
        f"Reddit Data:\n{raw}\n\n"
        "Now generate the full user persona in plain text."
    )


def call_openai(prompt, key):
    openai.api_key = key
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Reddit data analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        return resp["choices"][0]["message"]["content"]
    except Exception as exc:
        print("OpenAI error:", exc)
        return None


def save_persona(username, content):
    Path(f"{username}.txt").write_text(content, encoding="utf-8")
    print(f"Persona saved as {username}.txt")


def main():
    creds = load_credentials()
    reddit = get_reddit_client(creds)
    url = input("Enter Reddit profile URL: ").strip()
    username = extract_username(url)
    print(f"Scraping u/{username} ...")
    posts, comments = scrape_user_content(reddit, username)
    if not posts and not comments:
        print("No data found.")
        return
    print("Generating persona ...")
    persona = call_openai(build_prompt(posts, comments), creds["openai_api_key"])
    if persona:
        save_persona(username, persona)
    else:
        print("Failed to generate persona.")


if __name__ == "__main__":
    main()