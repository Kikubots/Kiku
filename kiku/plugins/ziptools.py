# © ultroid
import glob
import os
import time

from . import *


@Lion.on(admin_cmd(pattern="zip ?(.*)"))
async def zipp(event):
    reply = await event.get_reply_message()
    t = time.time()
    if not reply:
        await eor(event, "яερℓү αηү мε∂ια σя ∂σcυмεηт.")
        return
    xx = await eor(event, "`ωαιт ℓεммε Pяσcεssιηg...`")
    if reply.media:
        if hasattr(reply.media, "document"):
            file = reply.media.document
            image = await downloader(
                reply.file.name,
                reply.media.document,
                xx,
                t,
                "ωαιт ℓεммε ∂σωηℓσα∂ιηg...",
            )
            file = image.name
        else:
            file = await event.download_media(reply)
    inp = file.replace(file.split(".")[-1], "zip")
    await bash(f"zip -r {inp} {file}")
    k = time.time()
    xxx = await uploader(inp, inp, k, xx, "ωαιт ℓεммε υρℓσα∂...")
    await borg.send_file(
        event.chat_id,
        xxx,
        force_document=True,
        thumb="resources/Lion.jpg",
        caption=f"`{xxx.name}`",
        reply_to=reply,
    )
    os.remove(inp)
    os.remove(file)
    await xx.delete()


@Lion.on(admin_cmd(pattern="unzip ?(.*)"))
async def unzipp(event):
    reply = await event.get_reply_message()
    t = time.time()
    if not reply:
        await eor(event, "яερℓү тσ αηү мε∂ια σя ∂σcυмεηт.")
        return
    xx = await eor(event, "`ωαιт ℓεммε ρяσcεss...`")
    if reply.media:
        if hasattr(reply.media, "document"):
            file = reply.media.document
            mime_type = file.mime_type
            if "application" not in mime_type:
                return await xx.edit("`яερℓү тσ αηү zιρ ғιℓε`")
            image = await downloader(
                reply.file.name, reply.media.document, xx, t, "ℓεммε ∂σωηℓσα∂..."
            )
            file = image.name
            if not file.endswith(("zip", "rar", "exe")):
                return await xx.edit("`яερℓү тσ αηү zιρ ғιℓε σηℓү`")
        else:
            return await xx.edit("`яερℓү тσ αηү zιρ ғιℓε σηℓү`")
    if not os.path.isdir("unzip"):
        os.mkdir("unzip")
    else:
        os.system("rm -rf unzip")
        os.mkdir("unzip")
    await bash(f"7z x {file} -aoa -ounzip")
    ok = glob.glob("unzip/*")
    k = []
    for x in ok:
        if os.path.isdir(x):
            k.append(x)
            break
    if k:
        await xx.edit(
            "үσυя υηzιρρε∂ ғιℓε sαvε∂ ιη `unzip` ғσℓ∂εя.\n∂σ `{i}ls unzip` and browse storage\nUse `{i}ul <path>` To upload.".format(
                i=HNDLR
            )
        )
    else:
        for x in ok:
            k = time.time()
            xxx = await uploader(x, x, k, xx, "υρℓσα∂ιηg...")
            await ultroid_bot.send_file(
                event.chat_id,
                xxx,
                force_document=True,
                thumb="resources/lion.jpg",
                caption=f"`{xxx.name}`",
            )
        await xx.delete()


@Lion.on(admin_cmd(pattern="addzip ?(.*)"))
async def azipp(event):
    reply = await event.get_reply_message()
    t = time.time()
    if not reply:
        await eor(event, "яερℓү тσ αηү мε∂ια σя ∂σcυмεηт.")
        return
    xx = await eor(event, "`ℓεммε ρяσcεss...`")
    if not os.path.isdir("zip"):
        os.mkdir("zip")
    if reply.media:
        if hasattr(reply.media, "document"):
            file = reply.media.document
            image = await downloader(
                "zip/" + reply.file.name,
                reply.media.document,
                xx,
                t,
                "נυsт α sεcση∂ ℓεммε ∂σωηℓσα∂...",
            )
            file = image.name
        else:
            file = await event.download_media(reply.media, "zip/")
    await xx.edit(f"∂σωηℓσα∂ε∂ `{file}` sυccsғυℓℓү...\n©тεαм ℓιση")


@Lion.on(admin_cmd(pattern="dozip ?(.*)"))
async def do_zip(event):
    if not os.path.isdir("zip"):
        return await eor(
            event, "First All Files Via {i}addzip then doZip to zip all files at one."
        )
    xx = await eor(event, "`processing`")
    await bash(f"zip -r ultroid.zip zip/*")
    k = time.time()
    xxx = await uploader("lionub.zip", "lionub.zip", k, xx, "υρℓσα∂ιηg...")
    await ultroid_bot.send_file(
        event.chat_id,
        xxx,
        force_document=True,
        thumb="resources/lion.jpg",
    )
    os.system("rm -rf zip")
    os.remove("lionub.zip")
    await xx.delete()
