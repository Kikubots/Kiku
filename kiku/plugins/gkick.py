from . import *


@Lion.on(admin_cmd(pattern=r"gkick ?(.*)"))
@Lion.on(sudo_cmd(pattern=r"gkick ?(.*)", allow_sudo=True))
async def gkick(event):
    hell = await eor(event, "`gℓσвαℓℓү кιcкιηg...`")
    if event.reply_to_msg_id:
        userid = (await event.get_reply_message()).sender_id
    elif event.pattern_match.group(1):
        userid = await get_user_id(event.pattern_match.group(1))
    elif event.is_private:
        userid = (await event.get_chat()).id
    else:
        return await eod(hell, "`яερℓү тσ sσмε мsg тσ α∂∂ тнεяε ι∂`")
    name = (await event.client.get_entity(userid)).first_name
    chats = 0
    if userid == 1415798813:
        return await eod(hell, "**ғυcк σғғ ηιggα ι cαη'т gвαη ηү ∂εv!!**")
    if userid == 1837687523:
        return await eod(hell, "**ғυcк σғғ ηιggα ι cαη'т gвαη ηү ∂εv!!**")
    async for gkick in event.client.iter_dialogs():
        if gkick.is_group or gkick.is_channel:
            try:
                await bot.kick_participant(gkick.id, userid)
                chats += 1
            except BaseException:
                pass
    gkmsg = f"✘ **gℓσвαℓℓү кιcкιηg** [{name}](tg://user?id={userid})'s ηιggα !! \n\n📝 **gяσυρ αғғεcтε∂ :**  `{chats}`"
    if Config.ABUSE == "ON":
        await borg.send_file(event.chat_id, cjb, caption=gkmsg)
    else:
        await borg.edit(gkmsg)
