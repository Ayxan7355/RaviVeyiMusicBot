from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("22362834"))
API_HASH = getenv("0118f304bec8779e7e0480d1be5b0dd3")

BOT_TOKEN = getenv("BOT_TOKEN", "6969130767:AAHnRo60zabWcDScDhHCj5A1bxoLKHkuuUY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("5469476479"))

PING_IMG = getenv("PING_IMG", "https://images.app.goo.gl/czQH55rn8y2Jk4is5")
START_IMG = getenv("START_IMG", "https://images.app.goo.gl/hvRp5UsR8j3z2wcB9")

SESSION = getenv("SESSION", "AgFVOtIAFt_vLSDveokGIoZeSZRwdbyjOE9A7NPfO5-36T1d-C70QKysUFC7Lf9pKw32_57CxAM3T9w37h-Ged5hx_KyzKKoK7Kk_Co0u-x0aJd8DEBOaSl8BmAOpUwx0wOXUpYqssETa_qenBBn6CugrhpXymicEPpjhE8TTDL978HeGhHyQ2uilUd9BXitFHN19WZspu_B15TYuyEH4XNGkfpHnIYXpPp2ZEOQT3_Isnfr3ZkB1_RFD1JXZMF18TYcdv6W7lKCPVxqTI_Hvmdszw9YCkgP2eXAYCzO6VdJwsas9Qj8qy-MpdnG5KKzy45bzldhb4hYvIxZH8pYWbiMttdeKgAAAAGm0rk2AA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TechnoQurup1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TechnoKanal1")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5469476479").split()))


FAILED = "https://images.app.goo.gl/czQH55rn8y2Jk4is5"
