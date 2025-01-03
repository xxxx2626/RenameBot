import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "22182189")
    API_HASH  = os.environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7523460888:AAFDvxGfTAibb8y692vPVr0kS27AFWuQAzI") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://aman991932:aman@cluster0.18hv15a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/AHL.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5977931010').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "AV_BOTz_UPDATE") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002110971750"))
    BIN_CHANNEL = int(os.environ.get("BIN_CHANNEL", "-1001973960964"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))

class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴀɪ {} 👋,
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.
➻ You Can Also Convert Video To File And File To Video.
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

ʙʏ : <a href=https://t.me/AV_BOTz_UPDATE>**ᴀᴠ ʙᴏᴛᴢ ᴜᴘᴅᴀᴛᴇ**</a></b>"""
    
    ABOUT_TXT = """<b>╔═══❰ <a href='https://t.me/AV_RENAME_BOT'>ᴀᴠ ʀᴇɴᴀᴍᴇ ʙᴏᴛ</a> ❱═❍
║╭━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : {}
║┣⪼👦ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/AV_OWNER_BOT'>ᴀᴠ ᴄʜᴀᴛ ᴏᴡɴᴇʀ</a>
║┣⪼❣️ᴜᴘᴅᴀᴛᴇ : <a href=https://t.me/AV_BOTz_UPDATE>ᴀᴠ ʙᴏᴛᴢ</a>
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ 3</a>
║┣⪼📚ʟɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a> 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : v2.01.1
║╰━━━━━━━━━━━━━━➣
╚═════════════════❍ </b>"""
    
    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•»</b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•»</b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•»</b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.

📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•»</b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ.
<b>•»</b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ.
<b>•»</b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ.

Exᴀᴍᴩʟᴇ:- /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>

<b>•»</b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].</a>
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""


