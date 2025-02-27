# kiku

# Copyright (C) 2020 Adek Maulana.
# All rights reserved.
"""
   Heroku manager for your userbot
"""

import asyncio
import math
import os

import heroku3
import requests

from kiku import CMD_HELP, CMD_HNDLR

Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"


@kiku.on(admin_cmd(pattern=r"(set|get|del) var (.*)", outgoing=True))
async def variable(var):
    """
    Manage most of ConfigVars setting, set new var, get current var,
    or delete var...
    """
    if Var.HEROKU_APP_NAME is not None:
        app = Heroku.app(Var.HEROKU_APP_NAME)
    else:
        return await edit_or_reply(
            var, "`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**"
        )
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        toput = await edit_or_reply(var, "`Getting information...`")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await toput.edit(
                    "**ConfigVars**:" f"\n\n`{variable} = {heroku_var[variable]}`\n"
                )
            return await toput.edit(
                "**ConfigVars**:" f"\n\n`Error:\n-> {variable} don't exists`"
            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await bot.send_file(
                        var.chat_id,
                        "configs.json",
                        reply_to=var.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await toput.edit(
                        "`[HEROKU]` ConfigVars:\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================"
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        toput = await edit_or_reply(var, "`Setting information...`")
        if not variable:
            return await toput.edit("`.set var <ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await toput.edit(f"`{CMD_HNDLR}set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await toput.edit(f"`{variable}` **successfully changed to **`{value}`")
        else:
            await toput.edit(
                f"`{variable}`** successfully added with value` **{value}`"
            )
        heroku_var[variable] = value
    elif exe == "del":
        toput = await edit_or_reply(var, "`Getting information to delete variable...`")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await toput.edit("`Please specify ConfigVars you want to delete`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await toput.edit(f"`{variable}` **has been successfully deleted**")
            del heroku_var[variable]
        else:
            return await toput.edit(f"`{variable}`** doesn't exist**")


@kiku.on(admin_cmd(pattern="usage"))
@kiku.on(sudo_cmd(pattern="usage", allow_sudo=True))
async def dyno_usage(dyno):
    """
    Get your account Dyno Usage
    """
    dyno = await eor(dyno, "`Processing...`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Var.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit(
            "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    # - Used -
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    # - Current -
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(
        "**⚙️ Dyno Usage ⚙️**:\n\n"
        f" -> `Dyno usage for`  **{Var.HEROKU_APP_NAME}**:\n"
        f"     •  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        " -> `Dyno hours quota remaining this month`:\n"
        f"     •  `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  [`{percentage}`**%**]"
    )


@kiku.on(admin_cmd(pattern="info heroku"))
@kiku.on(sudo_cmd(pattern="info heroku", allow_sudo=True))
async def info(event):
    await borg.send_message(
        event.chat_id,
        "**Info for Module to Manage Heroku:**\n\n`.usage`\nUsage:__Check your heroku dyno hours status.__\n\n`.set var <NEW VAR> <VALUE>`\nUsage: __add new variable or update existing value variable__\n**!!! WARNING !!!, after setting a variable the bot will restart.**\n\n`.get var or .get var <VAR>`\nUsage: __get your existing varibles, use it only on your private group!__\n**This returns all of your private information, please be cautious...**\n\n`.del var <VAR>`\nUsage: __delete existing variable__\n**!!! WARNING !!!, after deleting variable the bot will restarted**",
    )
    await event.delete()


def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""

    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)


@kiku.on(admin_cmd(outgoing=True, pattern=r"logs"))
@kiku.on(sudo_cmd(allow_sudo=True, pattern=r"logs"))
async def _(givelogs):
    try:
        Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
        app = Heroku.app(Var.HEROKU_APP_NAME)
    except BaseException:
        return await eor(
            givelogs,
            " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var !",
        )
    await eor(givelogs, "Downloading Logs..")
    with open("logs-Lion.txt", "w") as log:
        log.write(app.get_log())
    ok = app.get_log()
    message = ok
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    await givelogs.client.send_file(
        givelogs.chat_id,
        "logs-Lion.txt",
        reply_to=givelogs.id,
        caption=f"**Heroku** Lion Logs.\nPasted [here]({url}) too!",
    )
    await eor(givelogs, "Heroku Logs Incoming!!")
    await asyncio.sleep(5)
    await givelogs.delete()
    return os.remove("logs-Lion.txt")


CMD_HELP.update(
    {
        "heroku": ".set var <name> <value>\nUse - Set the variable with the value given.\
        \n\n.get var <name>\nUse - Get the value of that variable.\
        \n\n.usage\nUse - See your heroku dyno usage.\
        \n\n.logs\nUse - Get your heroku logs."
    }
)
