"""call
Available Commands:
.call
"""
import asyncio

from telethon import events

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@thunderuserbot"


@borg.on(admin_cmd(pattern=r"call"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    # input_str = event.pattern_match.group(1)

    # if input_str == "call":

    await event.edit("Calling")

    animation_chars = [
        "**Connecting To Telegram Headquarters...**",
        "**Call Connected.**",
        "**Telegram: Hello This is Telegram HQ. Who is this?**",
        f"**Me: Yo this is** {DEFAULTUSER} ,**Please Connect me to THUNDERGANG**",
        "**User Authorised.**",
        "**Calling THUNDERGANG At +16827928983792**",
        "**Private  Call Connected...**",
        "**Me: Hello Sir, Please Ban This Telegram Account.**",
        "**THUNDERGANG : May I Know Who Is This?**",
        f"**Me: SIR, I Am** {DEFAULTUSER}",
        "**THUNDERGANG: OMG!!! Long time no see, How are you Brother...**\n**Please talk to nucleo support they can help you in banning.**",
        "**Me: Thanks, I will talk to them but where?.**",
        "**Pavel: You can talk to them at their support group on telegram https://t.me/Nucleosupportchat.**",
        "**Pavel: Sure Sir**\n**Take Care Bye :)**",
        "**Private Call Disconnected.**",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])
