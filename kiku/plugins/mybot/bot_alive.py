

import os
from telethon import Button, events

from Lion import ALIVE_NAME, bot

currentversion = "2.1"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓιση x υsεт"
ASSIS_PIC = os.environ.get("ASSIS_PIC", None)
if ASSIS_PIC is None:
    PM_IMG = "https://telegra.ph/file/af3b74010808a26480693.jpg"
else:
    PM_IMG = ASSIS_PIC


pm_caption = " ►**ɦɛʏʏ ʏօʊʀ ǟֆֆɨֆȶǟռȶ ɨֆ `օռʟɨռɛ`\n\n"
pm_caption += "► **Sʏsᴛᴇᴍ sᴛᴀᴛs**\n"
pm_caption += "► **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ:** `1.21.1` \n"
pm_caption += f"► **Lɪᴏɴ X ᴀssɪᴛᴀɴᴛ ᴠᴇʀsɪᴏɴ** : `{currentversion}`\n"
pm_caption += f"► **Mʏ ᴍᴀsᴛᴇʀ** : {DEFAULTUSER} \n"
pm_caption += "► **Lɪᴏɴ X ʟɪᴄᴇɴsᴇ** : [GNU General Public License v3.0](https://github.com/teamlion-X/Lion-X/blob/master/LICENSE)\n"
pm_caption += "► **Cᴏᴘʏʀɪɢʜᴛ** :[LɪᴏɴX](https://github.com/teamlion-X/Lion-X)\n"
light = [[Button.url("✧ʀᴇᴘᴏsɪᴛᴏʀʏ✧",
                     "https://github.com/teamlion-X/Lion-X"),
          Button.url("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ",
                     "https://t.me/LionXSupport")]]


@tgbot.on(events.NewMessage(pattern="^/alive",
                            func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption, buttons=light)
