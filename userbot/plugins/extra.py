import asyncio
import time
from collections import deque

from telethon.tl.functions.channels import LeaveChannelRequest

from userbot import bot
from userbot import BOTLOG
from userbot import BOTLOG_CHATID
from userbot import CMD_HELP
from userbot.utils import admin_cmd


@borg.on(admin_cmd("leave$"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I AM LEAVING THIS GROUP!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`This is Not A Chat`")


@borg.on(admin_cmd(";__;$"))
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)


@borg.on(admin_cmd("yo$"))
async def Ooo(e):
    t = "yo"
    for j in range(15):
        t = t[:-1] + "oo"
        await e.edit(t)


@borg.on(admin_cmd("Oof$"))
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)


@borg.on(admin_cmd("ccry$"))
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")


@borg.on(admin_cmd("fp$"))
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")


@borg.on(admin_cmd("moon$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd("source$"))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/Thundergang/thunderuserbot")


@borg.on(admin_cmd("readme$"))
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "https://github.com/Thundergang/thunderuserbot/blob/master/README.md")


@borg.on(admin_cmd("heart$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd("fap$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🍆✊🏻💦"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


CMD_HELP.update({"leave": "Leave a Chat"})
CMD_HELP.update({";__;": "You try it!"})
CMD_HELP.update({"cry": "Cry"})
CMD_HELP.update({"fp": "Send face palm emoji."})
CMD_HELP.update({"moon": "Bot will send a cool moon animation."})
CMD_HELP.update({"clock": "Bot will send a cool clock animation."})
CMD_HELP.update({"readme": "Reedme."})
CMD_HELP.update({"source": "Gives the source of your userbot"})
CMD_HELP.update({"myusernames": "List of Usernames owned by you."})
CMD_HELP.update({"oof": "Same as ;__; but ooof"})
CMD_HELP.update({"earth": "Sends Some animation"})
CMD_HELP.update({"heart": "Try and you'll get your emotions back"})
CMD_HELP.update({"fap": "Faking orgasm"})
