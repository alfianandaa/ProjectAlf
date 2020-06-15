# Copyright (C) 2020 alfiananda84
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r'^.anime(:? |$)(.*)?')
async def anime(anm):
    await anm.edit("`Sending information...`")
    level = anm.pattern_match.group()
    if anm.fwd_from:
        return
    if not anm.reply_to_msg_id:
        await anm.edit("`Reply To any Images/videos/Gifs`")
        return
    reply_message = await anm.get_reply_message()
    if not reply_message.media:
        await anm.edit("`Reply To any Images/videos/Gifs`")
        return
    if reply_message.sender.bot:
        await anm.edit("`Reply to actual user...`")
        return
    chat = "@YuiChanBot"
    await anm.edit("```Getting Your Anime Info....```")
    message_id_to_reply = anm.message.reply_to_msg_id
    msg_reply = None
    async with anm.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=601294817))
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/whatanime"
                msg_reply = await conv.send_message(
                          m,
                          reply_to=msg.id)
                r = await conv.get_response()
                response = await response
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await anm.reply("`Please unblock` @YuiChanBot`...`")
            return
        else:
            await anm.client.send_message(
                anm.chat_id, 
                response.message,
                reply_to=message_id_to_reply
            )
            await anm.client.delete_messages(conv.chat_id,
                    [msg.id, msg_reply.id, r.id, response.id])

    await anm.delete()

CMD_HELP.update({
        "anime": 
        ">`.anime`"
        "\nUsage: Reply a image/gif/video to check what anime it is from."
    })
