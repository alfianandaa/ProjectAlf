# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import os

from telethon.tl.types import DocumentAttributeFilename

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.ssvideo(?: |$)(.*)")
async def ssvideo(event):
    if not event.reply_to_msg_id:
        await event.edit("`Reply to any media..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`reply to a video..`")
        return
    try:
        frame = int(event.pattern_match.group(1))
        if frame > 10:
            return await event.edit("`hey..dont put that much`")
    except BaseException:
        return await event.edit("`Please input number of frame!`")
    await event.edit("`Downloading media..`")
    file = os.path.join(TEMP_DOWNLOAD_DIRECTORY, "")
    ss = await bot.download_media(
        reply_message,
        file,
    )
    if (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in message.media.document.attributes
    ):
        await gifify(ss, 215)
    try:
        await event.edit("`Proccessing..`")
        command = f"vcsi -g {frame}x{frame} {ss} -o ss.png "
        os.system(command)
        await event.client.send_file(
            event.chat_id,
            "ss.png",
            reply_to=event.reply_to_msg_id,
        )
        await event.delete()
        os.system("rm -rf *.png")
        os.system("rm -rf *.mp4")
    except BaseException as e:
        os.system("rm -rf *.png")
        os.system("rm -rf *.mp4")
        return await event.edit(f"{e}")


async def gifify(sticker_path: str, quality: int = 256) -> str:
    dest = os.path.join(TEMP_DOWNLOAD_DIRECTORY, "animation.gif")
    with open(dest, "wb") as t_g:
        lottie.exporters.gif.export_gif(
            lottie.parsers.tgs.parse_tgs(sticker_path), t_g, quality, 1
        )
    os.remove(sticker_path)
    return dest


CMD_HELP.update(
    {"ssvideo": "`>.ssvideo <frame>`" "\nUsage: to ss video frame per frame"}
)
