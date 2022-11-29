import os
from emoji import emojize
import local_settings

# TG bot token
TOKEN = local_settings.TOKEN

# DB name
NAME_DB = 'products.db'

# App version
VERSION = '0.0.1'

# App author
AUTHOR = 'Dmytro'

# Parent directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# DB path
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# TG bot keyboard buttons
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Choose a good'),
    'INFO': emojize(':speech_balloon: Shop info'),
    'SETTINGS': emojize('⚙️ Settings'),
    'SEMIPRODUCT': emojize(':pizza: Ready-to-cook food'),
    'GROCERY': emojize(':bread: Grocery'),
    'ICE_CREAM': emojize(':shaved_ice: Ice Cream'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ORDER'),
    'X': emojize('❌'),
    'DOWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLY': '✅ Place an order',
    'COPY': '©️'
}

# id of product categories
CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

# Commands name
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
