"""
from os import getenv


API_ID = int(getenv("API_ID", "28031075"))
API_HASH = getenv("API_HASH", "6a309d42eda281416f798a554360e6a8")
BOT_TOKEN = getenv("BOT_TOKEN", "7361708263:AAECkqJCTVtGWMXReznsMUAXhwbazRH1Pko")
OWNER_ID = int(getenv("OWNER_ID", "5829511291"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5457168404 5829511291").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://om:om@cluster0.skybyiv.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002154140916"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002154140916"))

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

