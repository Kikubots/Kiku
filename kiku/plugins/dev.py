import asyncio

from kiku.utils import admin_cmd


@kiku.on(admin_cmd(pattern="(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.01
    animation_ttl = range(0, 288)
    input_str = event.pattern_match.group(1)
    if input_str == "dev":
        await event.edit(input_str)
        animation_chars = [
            "M_ ____",
            "MD ____",
            "MD N___",
            "MD NO__",
            "MD NOO_",
            "MD NOOR",
            "**ANOTHER ONE**",
            "S_______",
            "SH______",
            "SHA_____",
            "SHAS____",
            "SHASH___",
            "SHASHA__",
            "SHASHAN_",
            "SHASHANK",
            "**AND**",
            "K_______",
            "KE______",
            "KEI_____",
            "KEIN____",
            "KEINS___",
            "KEINSH__",
            "KEINSHI_",
            "KEINSHIN",
            "MD NOOR SHASHANK KEINSHIN THESE ARE MY PERU DEV",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 72])
