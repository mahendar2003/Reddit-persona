import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

print("🔐 Values loaded:")
print("CLIENT_ID =", os.getenv("REDDIT_CLIENT_ID"))
print("CLIENT_SECRET =", os.getenv("REDDIT_CLIENT_SECRET"))
print("USER_AGENT =", os.getenv("REDDIT_USER_AGENT"))

print("🧪 Testing reddit access...")
print("Read-only mode:", reddit.read_only)
