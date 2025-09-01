#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25271265"))
API_HASH = environ.get("API_HASH", "2b444dd24960df5a274aea08bf62cf8e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8062036208:AAHgwAy7c2vapA-h96lDXKXxLQUX4hkI1b0")

OWNER = int(environ.get("OWNER", "5765708156"))
CREDIT = environ.get("CREDIT", "[『 𝗧𝗚𝖩ᴏᴋᴇʀ𝗫 🎭』](https://t.me/TGJokerX)")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5765708156').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5765708156').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


