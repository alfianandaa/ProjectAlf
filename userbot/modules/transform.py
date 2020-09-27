# Authored by @Khrisna_Singhal
# Ported from Userge by Alfiananda P.A

import os

from PIL import Image, ImageOps

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register
from userbot.utils import check_media

Converted = TEMP_DOWNLOAD_DIRECTORY + "sticker.webp"


@register(outgoing=True, pattern=r"^\.(mirror|flip|ghost|bw|poster)$")
async def transform(event):
    if not event.reply_to_msg_id:
        await event.edit("`Reply to Any media..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`reply to a image/sticker`")
        return
    if event.is_reply:
        data = await check_media(reply_message)
        if isinstance(data, bool):
            await event.edit("`Unsupported Files...`")
            return
    await event.edit("`Downloading Media..`")
    downloaded_file_name = os.path.join(TEMP_DOWNLOAD_DIRECTORY, "gambar.png")
    transform = await bot.download_media(
        reply_message,
        downloaded_file_name,
    )
    try:
        await event.edit("`Transforming this image..`")
        cmd = event.pattern_match.group(1)
        im = Image.open(transform).convert("RGB")
        if cmd == "mirror":
            IMG = ImageOps.mirror(im)
        elif cmd == "flip":
            IMG = ImageOps.flip(im)
        elif cmd == "ghost":
            IMG = ImageOps.invert(im)
        elif cmd == "bw":
            IMG = ImageOps.grayscale(im)
        elif cmd == "poster":
            IMG = ImageOps.posterize(im, 2)
        IMG.save(Converted, quality=95)
        await event.client.send_file(
            event.chat_id, Converted, reply_to=event.reply_to_msg_id
        )
        await event.delete()
        os.remove(transform)
        os.remove(Converted)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.rotate(?: |$)(.*)")
async def rotate(event):
    if not event.reply_to_msg_id:
        await event.edit("`Reply to any media..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`reply to a image/sticker`")
        return
    if event.is_reply:
        data = await check_media(reply_message)
        if isinstance(data, bool):
            await event.edit("`Unsupported Files...`")
            return
    await event.edit("`Downloading Media..`")
    downloaded_file_name = os.path.join(TEMP_DOWNLOAD_DIRECTORY, "gambar.png")
    rotate = await bot.download_media(
        reply_message,
        downloaded_file_name,
    )
    await event.edit("`Rotating your media..`")
    try:
        value = int(event.pattern_match.group(1))
        if value > 360:
            raise ValueError
    except ValueError:
        value = 90
    im = Image.open(rotate).convert("RGB")
    IMG = im.rotate(value, expand=1)
    IMG.save(Converted, quality=95)
    await event.client.send_file(
        event.chat_id, Converted, reply_to=event.reply_to_msg_id
    )
    await event.delete()
    os.remove(rotate)
    os.remove(Converted)


CMD_HELP.update(
    {
        "transform": ">`.ghost`"
        "\nUsage: Enchance your image to become a ghost!."
        "\n\n>`.flip`"
        "\nUsage: To flip your image"
        "\n\n>`.mirror`"
        "\nUsage: To mirror your image"
        "\n\n>`.bw`"
        "\nUsage: To Change your colorized image to b/w image!"
        "\n\n>`.poster`"
        "\nUsage: To posterize your image!"
        "\n\n>`.rotate <value>`"
        "\nUsage: To rotate your image\n* The value is range 1-360 if not it'll give default value which is 90"
    }
)
