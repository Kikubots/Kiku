import asyncio

from kiku import CMD_HELP
from kiku.plugins.sql_helper.mute_sql import is_muted, mute, unmute
from kiku.utils import admin_cmd


@kiku.on(admin_cmd(outgoing=True, pattern=r"gmute ?(\d+)?"))
@kiku.on(sudo_cmd(allow_sudo=True, pattern=r"gmute ?(\d+)?"))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await eor(event, "Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await eor(
            event, "Please reply to a user or add their into the command to gmute them."
        )
    event.chat_id
    await event.get_chat()
    if is_muted(userid, "gmute"):
        return await eor(event, "тнιѕ υѕєя ιѕ αℓяєα∂у gмυтє∂")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await eor(event, "Error occured!\nError is " + str(e))
    else:
        await eor(event, "Silence now. **ѕυ¢¢єѕѕfυℓℓу fυ¢кє∂ тнιѕ иιggα мσυтн**")


@kiku.on(admin_cmd(outgoing=True, pattern=r"ungmute ?(\d+)?"))
@kiku.on(sudo_cmd(allow_sudo=True, pattern=r"ungmute ?(\d+)?"))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await eor(event, "Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await eor(
            event,
            "Please reply to a user or add their into the command to ungmute them.",
        )
    event.chat_id
    if not is_muted(userid, "gmute"):
        return await eor(event, "тнιѕ υѕєя ιѕ иσт gмυтє∂")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await eor(event, "Error occured!\nError is " + str(e))
    else:
        await eor(event, "ѕυ¢¢єѕѕfυℓℓу ∂σиє уσυя тσ∂αу fυ¢к иσω gσ")


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


CMD_HELP.update(
    {
        "gmute": ".gmute <reply to user>\nUse - Globally mute the person (across all chats).\
        \n\n.ungmute <reply to user>\nUse - Globally UnMute the person."
    }
)
