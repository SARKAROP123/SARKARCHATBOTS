from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "6435225"
# -------------------------------------------------------------
API_HASH = "4e984ea35f854762dcde906dce426c2d"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "6919772024"))
SUPPORT_GRP = "TG_NAME_STYLE"
UPDATE_CHNL = "TG_NAME_STYLE"
OWNER_USERNAME = "ll_SARKAR_MERA_BABU_ll"
