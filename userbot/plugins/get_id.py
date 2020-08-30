"""Get ID of any Telegram media, or any user
Syntax: .get_id"""
from telethon import events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantsBots
from telethon.utils import pack_bot_file_id

from userbot.utils import admin_cmd


@borg.on(admin_cmd("get_id"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        chat = await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.edit(
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`"
                .format(str(event.chat_id), str(r_msg.from_id),
                        bot_api_file_id))
        else:
            await event.edit(
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id)))
    else:
        await event.edit("Current Chat ID: `{}`".format(str(event.chat_id)))


""" Get the Bots in any chat*
Syntax: .get_bot"""


@borg.on(admin_cmd("get_bot ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Bots in this Channel**: \n"
    input_str = event.pattern_match.group(1)
    to_write_chat = await event.get_input_chat()
    chat = None
    if not input_str:
        chat = to_write_chat
    else:
        mentions = "Bots in {} channel: \n".format(input_str)
        try:
            chat = await borg.get_entity(input_str)
        except Exception as e:
            await event.edit(str(e))
            return None
    try:
        async for x in borg.iter_participants(chat,
                                              filter=ChannelParticipantsBots):
            if isinstance(x.participant, ChannelParticipantAdmin):
                mentions += "\n ⚜️ [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id)
            else:
                mentions += "\n [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id)
    except Exception as e:
        mentions += " " + str(e) + "\n"
    await event.edit(mentions)
