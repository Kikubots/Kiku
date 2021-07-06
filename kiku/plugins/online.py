# Copyright Lion
# For @LionHelp coded by @xditya
# Kangers keep credits else I'll take down 🧐

import random
import sys

from telethon import version

from Lion import ALIVE_NAME
from Lion.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lion User"

ONLINESTR = [
    "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n█░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░█  █░║║║╠─║─║─║║║║║╠─░█ \n█░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░█ \n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ \n\n**Lion is online.**\n\n**All systems functioning normally !** \n\n**Bot by** [Team Lion](tg://user?id=1837687523) \n\n**More help -** @LionXUpdates \n\n           [🚧 GitHub Repository 🚧](https://github.com/TeamLion-X/Lion-X)",
    f"╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗\n║║║╠─║─║─║║║║║╠─\n╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝\n              **Welcome to Lion**\n\n**Hey master! I'm alive. All systems online and functioning normally ✅**\n\n**✔️ Telethon version:** `{version.__version__}` \n\n**✔️ Python:** `{sys.version}` \n\n✔️ More info: @LionXUpdates \n\n✔️ Created by: [Team Lion](tg://user?id1837687523=) \n\n**✔️ Database status:** All ok 👌 \n\n**✔️ My master:** {DEFAULTUSER} \n\n        [🌟 Github repository 🌟](https://github.com/TeamLion-X/Lion-X)",
]


@Lion.on(admin_cmd(outgoing=True, pattern="online"))
@Lion.on(sudo_cmd(allow_sudo=True, pattern="online"))
async def online(event):
    """ Greet everyone! """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await eor(event, random.choice(ONLINESTR))
