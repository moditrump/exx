"""
from os import getenv


API_ID = int(getenv("API_ID", "25274255"))
API_HASH = getenv("API_HASH", "02b2832c0e2cc02d8cf178c8a95a5d59")
BOT_TOKEN = getenv("BOT_TOKEN", "6837464911:AAGoReETsqhMEDexwcyA4QR2abOFbLvNBQ0")
OWNER_ID = int(getenv("OWNER_ID", "7103902728"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7103902728 2112898623").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001993672460"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1001993672460"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

