# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24935727"))
API_HASH = getenv("API_HASH", "3fd33336629324ecd664e9b6894f0909")
BOT_TOKEN = getenv("BOT_TOKEN", "7414447083:AAEnBqw4RdEmL8PauBsjlFggMwLpcmJTGrk")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7336971189").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sujay0089:sujay0089@cluster00899.gim8u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster00899")
LOG_GROUP = getenv("LOG_GROUP", "-1002262545667")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002483720229"))
