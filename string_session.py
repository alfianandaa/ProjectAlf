from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details""")

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    session_string = client.session.save()
    saved_messages_template = """<code>STRING_SESSION</code>: <code>{}</code>
️<i>It is forbidden to pass this value to third parties</i>""".format(session_string)
    client.send_message("me", saved_messages_template, parse_mode="html")
    print("Check Saved Messages on your telegram account !!")
