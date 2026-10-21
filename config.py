# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("8638713084:AAHT1QDyZT1LgyVGanJmhlyAmZlExTnxkJM", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "8963718797"))
GROUP_ID = int(os.getenv("GROUP_ID", "-1003689494017"))

USE_PROXY = False
PROXY_TYPE = "socks5"
PROXY_HOST = "127.0.0.1"
PROXY_PORT = 12334

CODE_PREFIX = "CP"
MAX_CP = 100000
CP_OPTIONS = [10000, 20000, 50000, 80000, 100000]
SUPPORT_ID = "Rubika.ir/sjsjsdjea"