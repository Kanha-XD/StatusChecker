<h1 align="center">sᴛᴀᴛᴜs ᴄʜᴇᴄᴋᴇʀ</h1>

<p align="center">
  <a href="https://t.me/incorrect_krishna">
    <img src="https://envs.sh/Gx8.jpg" width="300">
  </a>
</p>

<p align="center">
  <b>At least give a Star and Fork the repo</b>
</p>

## 📜 Plugin Code

Copy the following code and add it into your plugins directory:

```python
import psutil
import time
from pyrogram import Client, filters
from pyrogram.types import Message

start_time = time.time()

def time_formatter(milliseconds):
    minutes, seconds = divmod(int(milliseconds / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (((str(weeks) + "ᴡ:") if weeks else "") +
           ((str(days) + "ᴅ:") if days else "") +
           ((str(hours) + "ʜ:") if hours else "") +
           ((str(minutes) + "ᴍ:") if minutes else "") +
           ((str(seconds) + "s") if seconds else ""))
    if not tmp:
        return "0s"
    if tmp.endswith(":"):
        return tmp[:-1]
    return tmp


@Client.on_message(filters.command("statuscheck"))
async def status(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    TEXT = f"ᴜᴘᴛɪᴍᴇ : {uptime} | ᴄᴘᴜ : {cpu}%"
    await message.reply(TEXT)
```

---

## 🚀 Deploy on Heroku

<p align="center">
  <a href="https://dashboard.heroku.com/new?template=https://github.com/Kanha-XD/StatusChecker">
    <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-black?style=for-the-badge&logo=heroku" width="220"/>
  </a>
</p>

---

## ⚡ Deploy on VPS

1. Get your [Necessary Variables](https://github.com/Kanha-XD/StatusChecker/blob/main/sample.env)  
2. Update and upgrade:
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```
3. Install required packages:
   ```bash
   sudo apt-get install python3-pip
   ```
4. Upgrade pip:
   ```bash
   pip3 install -U pip
   ```
5. Clone the repository:
   ```bash
   git clone https://github.com/Kanha-XD/StatusChecker && cd StatusChecker
   ```
6. Install requirements:
   ```bash
   pip3 install -U -r requirements.txt
   ```
7. Fill in environment variables:
   ```bash
   vi sample.env
   ```
   Press <code>I</code> to edit, <code>Ctrl+C</code> when done, then type <code>:wq</code> to save.
8. Rename the env file:
   ```bash
   mv sample.env .env
   ```
9. Install tmux and start session:
   ```bash
   sudo apt install tmux && tmux
   ```
10. Run the bot:
    ```bash
    bash start
    ```

---

## 📦 Requirements

- Python 3.8+  
- [Pyrogram](https://docs.pyrogram.org/)  
- [psutil](https://pypi.org/project/psutil/)

---

## 💬 Support

<p align="center">
  <a href="https://telegram.me/RadhaSupport">
    <img src="https://img.shields.io/badge/-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram">
  </a>
</p>

<p align="center">
  <a href="https://telegram.me/RadhaUpdates">
    <img src="https://img.shields.io/badge/-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram">
  </a>
</p>
