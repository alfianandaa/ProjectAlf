# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# This module is maked by Project TESLA

from userbot import CMD_HELP
from userbot.events import register

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]
circlyfont = [
    "🅐",
    "🅑",
    "🅒",
    "🅓",
    "🅔",
    "🅕",
    "🅖",
    "🅗",
    "🅘",
    "🅙",
    "🅚",
    "🅛",
    "🅜",
    "🅝",
    "🅞",
    "🅟",
    "🅠",
    "🅡",
    "🅢",
    "🅣",
    "🅤",
    "🅥",
    "🅦",
    "🅧",
    "🅨",
    "🅩",
]
oldengfont = [
    "𝔄",
    "𝔅",
    "ℭ",
    "𝔇",
    "𝔈",
    "𝔉",
    "𝔊",
    "ℌ",
    "ℑ",
    "𝔍",
    "𝔎",
    "𝔏",
    "𝔐",
    "𝔑",
    "𝔒",
    "𝔓",
    "𝔔",
    "ℜ",
    "𝔖",
    "𝔗",
    "𝔘",
    "𝔙",
    "𝔚",
    "𝔛",
    "𝔜",
    "ℨ",
]
boldfont = [
    "𝗮",
    "𝗯",
    "𝗰",
    "𝗱",
    "𝗲",
    "𝗳",
    "𝗴",
    "𝗵",
    "𝗶",
    "𝗷",
    "𝗸",
    "𝗹",
    "𝗺",
    "𝗻",
    "𝗼",
    "𝗽",
    "𝗾",
    "𝗿",
    "𝘀",
    "𝘁",
    "𝘂",
    "𝘃",
    "𝘄",
    "𝘅",
    "𝘆",
    "𝘇",
]
medievalbold = [
    "𝖆",
    "𝖇",
    "𝖈",
    "𝖉",
    "𝖊",
    "𝖋",
    "𝖌",
    "𝖍",
    "𝖎",
    "𝖏",
    "𝖐",
    "𝖑",
    "𝖒",
    "𝖓",
    "𝖔",
    "𝖕",
    "𝖖",
    "𝖗",
    "𝖘",
    "𝖙",
    "𝖚",
    "𝖛",
    "𝖜",
    "𝖝",
    "𝖞",
    "𝖟",
]
doublestruckt = [
    "𝕒",
    "𝕓",
    "𝕔",
    "𝕕",
    "𝕖",
    "𝕗",
    "𝕘",
    "𝕙",
    "𝕚",
    "𝕛",
    "𝕜",
    "𝕝",
    "𝕞",
    "𝕟",
    "𝕠",
    "𝕡",
    "𝕢",
    "𝕣",
    "𝕤",
    "𝕥",
    "𝕦",
    "𝕧",
    "𝕨",
    "𝕩",
    "𝕪",
    "𝕫",
]
cursiveboldx = [
    "𝓪",
    "𝓫",
    "𝓬",
    "𝓭",
    "𝓮",
    "𝓯",
    "𝓰",
    "𝓱",
    "𝓲",
    "𝓳",
    "𝓴",
    "𝓵",
    "𝓶",
    "𝓷",
    "𝓸",
    "𝓹",
    "𝓺",
    "𝓻",
    "𝓼",
    "𝓽",
    "𝓾",
    "𝓿",
    "𝔀",
    "𝔁",
    "𝔂",
    "𝔃",
]
medival2 = [
    "𝔞",
    "𝔟",
    "𝔠",
    "𝔡",
    "𝔢",
    "𝔣",
    "𝔤",
    "𝔥",
    "𝔦",
    "𝔧",
    "𝔨",
    "𝔩",
    "𝔪",
    "𝔫",
    "𝔬",
    "𝔭",
    "𝔮",
    "𝔯",
    "𝔰",
    "𝔱",
    "𝔲",
    "𝔳",
    "𝔴",
    "𝔵",
    "𝔶",
    "𝔷",
]
cursive = [
    "𝒶",
    "𝒷",
    "𝒸",
    "𝒹",
    "𝑒",
    "𝒻",
    "𝑔",
    "𝒽",
    "𝒾",
    "𝒿",
    "𝓀",
    "𝓁",
    "𝓂",
    "𝓃",
    "𝑜",
    "𝓅",
    "𝓆",
    "𝓇",
    "𝓈",
    "𝓉",
    "𝓊",
    "𝓋",
    "𝓌",
    "𝓍",
    "𝓎",
    "𝓏",
]


@register(outgoing=True, pattern=r"^\.weeb(?: |$)(.*)")
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = "  ".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


@register(outgoing=True, pattern=r"^\.circ(?: |$)(.*)")
async def circly(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to circlyfy U Dumb`")
        return
    string = "  ".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            circlycharacter = circlyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, circlycharacter)
    await event.edit(string)


@register(outgoing=True, pattern=r"^\.oldeng(?: |$)(.*)")
async def oldy(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What, I am Supposed To Work with text only`")
        return
    string = "  ".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            oldycharacter = oldengfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, oldycharacter)
    await event.edit(string)


@register(outgoing=True, pattern=r"^\.bold(?: |$)(.*)")
async def thicc(bolded):

    args = bolded.pattern_match.group(1)
    if not args:
        get = await bolded.get_reply_message()
        args = get.text
    if not args:
        await bolded.edit("`What I am Supposed to bold for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            boldcharacter = boldfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, boldcharacter)
    await bolded.edit(string)


@register(outgoing=True, pattern=r"^\.medieval(?: |$)(.*)")
async def medival22(medivallite):

    args = medivallite.pattern_match.group(1)
    if not args:
        get = await medivallite.get_reply_message()
        args = get.text
    if not args:
        await medivallite.edit("`What I am Supposed to medival for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            medivalxxcharacter = medival2[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, medivalxxcharacter)
    await medivallite.edit(string)


@register(outgoing=True, pattern=r"^\.medievalbold(?: |$)(.*)")
async def mediv(medievalx):

    args = medievalx.pattern_match.group(1)
    if not args:
        get = await medievalx.get_reply_message()
        args = get.text
    if not args:
        await medievalx.edit("`What I am Supposed to medieval bold for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            medievalcharacter = medievalbold[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, medievalcharacter)
    await medievalx.edit(string)


@register(outgoing=True, pattern=r"^\.doublestruck(?: |$)(.*)")
async def doublex(doublestrucktx):

    args = doublestrucktx.pattern_match.group(1)
    if not args:
        get = await doublestrucktx.get_reply_message()
        args = get.text
    if not args:
        await doublestrucktx.edit("`What I am Supposed to double struck for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            strucktcharacter = doublestruckt[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, strucktcharacter)
    await doublestrucktx.edit(string)


@register(outgoing=True, pattern=r"^\.cursivebold(?: |$)(.*)")
async def cursive2(cursivebolded):

    args = cursivebolded.pattern_match.group(1)
    if not args:
        get = await cursivebolded.get_reply_message()
        args = get.text
    if not args:
        await cursivebolded.edit("`What I am Supposed to cursive bold for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursiveboldcharacter = cursiveboldx[normiefont.index(
                normiecharacter)]
            string = string.replace(normiecharacter, cursiveboldcharacter)
    await cursivebolded.edit(string)


@register(outgoing=True, pattern=r"^\.cursive(?: |$)(.*)")
async def xcursive(cursivelite):

    args = cursivelite.pattern_match.group(1)
    if not args:
        get = await cursivelite.get_reply_message()
        args = get.text
    if not args:
        await cursivelite.edit("`What I am Supposed to cursive for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursivecharacter = cursive[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, cursivecharacter)
    await cursivelite.edit(string)


CMD_HELP.update(
    {
        "fonts": ">`.weeb`"
        "\nUsage : weebifys your text. \n\n"
        ">`.circ`"
        "\nUsage : circlifies text.\n\n"
        ">`.oldeng`"
        "\nUsage : old eng font.\n\n"
        ">`.bold`"
        "\nUsage : bold your font.\n\n"
        ">`.medievalbold`"
        "\nUsage : medievalbold your font.\n\n"
        ">`.doublestruck`"
        "\nUsage : doublestruck your font.\n\n"
        ">`.cursive`"
        "\nUsage : cursive your font."
    }
)
