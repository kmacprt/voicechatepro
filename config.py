# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 1733305
API_HASH = "f423cffca6b5b7247b31b5b0df61f48d"

# Get this from @Botfather
TOKEN = "1410779822:AAGTXA6WeWFJ5DJ60axL4-dyC-wHDvP_U58"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1156597097,
]

# A group ID to send messages to when a song starts playing
# Example group ID: -1001402753006
LOG_GROUP = -1001290794905  # Just keep it like this if you are not going to use one

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for downloads in minutes
DUR_LIMIT = 50

# No need to touch the following.
SUDO_FILTER = filters.user(SUDO_USERS)
