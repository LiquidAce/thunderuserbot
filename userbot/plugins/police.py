
from telethon import events

import asyncio

from uniborg.util import admin_cmd

from userbot import ALIVE_NAME


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Thunderuserbot"

@borg.on(admin_cmd(pattern=r"police"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    await event.edit("Police")

    animation_chars = [
        
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",    
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "[Thunderuserbot](https://www.github.com/Thundergang/thunderuserbot) **Police iz Here**"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])
