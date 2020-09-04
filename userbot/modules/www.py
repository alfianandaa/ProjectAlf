# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

from datetime import datetime

from speedtest import Speedtest
from telethon import functions

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.speed$")
async def speedtst(spd):
    await spd.edit("`Running speed test . . .`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    output = f"Started at `{result['timestamp']}`\n\n"
    output += "`Client:`\n"
    output += f"ISP: `{result['client']['isp']}`\n"
    output += f"Country: `{result['client']['country']}`\n\n"
    output += "`Server:`\n"
    output += f"Name: `{result['server']['name']}`\n"
    output += f"Country: `{result['server']['country']}, {result['server']['cc']}`\n"
    output += f"Sponsor: `{result['server']['sponsor']}`\n"
    output += f"Latency: `{result['server']['latency']}`\n\n"
    output += "`Speed:`\n"
    output += f"Ping: `{result['ping']}`\n"
    output += f"Download: `{speed_convert(result['download'])}`\n"
    output += f"Upload: `{speed_convert(result['upload'])}` "
    await spd.delete()
    await spd.client.send_message(spd.chat_id, output)


def speed_convert(size):
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern=r"^\.dc$")
async def neardc(event):
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(
        f"Country : `{result.country}`\n"
        f"Nearest Datacenter : `{result.nearest_dc}`\n"
        f"This Datacenter : `{result.this_dc}`"
    )


@register(outgoing=True, pattern=r"^\.ping$")
async def pingme(pong):
    start = datetime.now()
    await pong.edit("`Pong!`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit("`Pong!\n%sms`" % (duration))


CMD_HELP.update(
    {
        "speed": ">`.speed`" "\nUsage: Does a speedtest and shows the results.",
        "dc": ">`.dc`" "\nUsage: Finds the nearest datacenter from your server.",
        "ping": ">`.ping`" "\nUsage: Shows how long it takes to ping your bot.",
    }
)
