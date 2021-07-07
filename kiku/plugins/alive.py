import asyncio
import time

from telethon import version
from userbot.utils import admin_cmd, sudo_cmd

from kiku import ALIVE_NAME, StartTime, lionver
from kiku.helper import functions as dcdef 
from kiku.LionConfig import Config, Var

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓιση x υsεя"

# Thanks to Sipak bro and Aryan..
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
# modded for kiku Userbot
global fuk
fuk = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/b637ae9a2a68b151e37c9.jpg"
""" =======================CONSTANTS====================== """
# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "Kiku ʊֆɛʀɮօȶ ɨֆ օռʟɨռɛ!"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else "https://telegra.ph/file/b637ae9a2a68b151e37c9.jpg"
lionemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**〢**"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#

@kiku.on(admin_cmd(pattern=r"alive"))
@kiku.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def hmm(yes):
    await yes.get_chat()
    global fuk
    fuk = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - StartTime))
    pm_caption = f"{lionemoji}**{CUSTOM_ALIVE}**\n\n"
    pm_caption += f"{lionemoji}**Mʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɢ**\n\n"
    pm_caption += f"{lionemoji} Aʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ ✗\n\n"
    pm_caption += f"{lionemoji} **My Pero Master** ☞ [{DEFAULTUSER}](tg://user?id={fuk})\n"
    pm_caption += f"{lionemoji} **Kiku VerSion**: `{lionver}`\n"
    pm_caption += f"{lionemoji} **TeleThon VerSion** ☞ {version.__version__}\n"
    pm_caption += f"{lionemoji} **SuPPort ChaNNel** ☞ [ᴊᴏɪɴ](https://t.me/Teamkiku)\n"
    pm_caption += f"{lionemoji} **LiCense**  ☞ [Team Kiku](https://github.com/teamkiku)\n"
    pm_caption += (
        f"{lionemoji} **©️ CopyRight By** ☞ [Kiku](https://github.com/teamkiku/kiku)\n\n"
    ) 
    pm_caption += f"{lionemoji} **Lion UpTime** ☞ {uptime}\n\n"
    on = await borg.send_file(
        yes.chat_id, file=ALV_PIC, caption=pm_caption, link_preview=False
    )

# This Alive is for Kiku modded from dc 
# use with credits
