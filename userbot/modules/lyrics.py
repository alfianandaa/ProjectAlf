# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
#

import codecs
import os

import lyricsgenius
import requests
from pylast import User

from userbot import CMD_HELP, GENIUS, LASTFM_USERNAME, lastfm
from userbot.events import register

if GENIUS is not None:
    genius = lyricsgenius.Genius(GENIUS)


@register(outgoing=True, pattern=r"^\.lyrics (?:(now)|(.*) - (.*))")
async def lyrics(lyric):
    await lyric.edit("`Getting information...`")
    if GENIUS is None:
        await lyric.edit("`Provide genius access token to Heroku ConfigVars...`")
        return False
    if lyric.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            await lyric.edit("`No information current lastfm scrobbling...`")
            return False
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = lyric.pattern_match.group(2)
        song = lyric.pattern_match.group(3)
    await lyric.edit(f"`Searching lyrics for {artist} - {song}...`")
    songs = genius.search_song(song, artist)
    if songs is None:
        await lyric.edit(f"`Song`  **{artist} - {song}**  `not found...`")
        return False
    if len(songs.lyrics) > 4096:
        await lyric.edit("`Lyrics is too big, pasted lyrics to Nekobin. please wait.`")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Search query: \n{artist} - {song}\n\n{songs.lyrics}")
        lirik = codecs.open("lyrics.txt", "r", encoding="utf-8")
        data = lirik.read()
        key = (requests.post("https://nekobin.com/api/documents",
                             json={"content": data}) .json() .get("result") .get("key"))
        url = f"https://nekobin.com/raw/{key}"
        await lyric.edit(f"`Here the lyrics:`\n\nPasted to: [Nekobin]({url})")
        os.remove("lyrics.txt")
    else:
        await lyric.edit(
            f"**Search query**:\n`{artist}` - `{song}`" f"\n\n```{songs.lyrics}```"
        )

    return True


CMD_HELP.update(
    {
        "lyrics": ">`.lyrics` **<artist name> - <song name>**"
        "\nUsage: Get lyrics matched artist and song."
        "\n\n>`.lyrics now`"
        "\nUsage: Get lyrics artist and song from current lastfm scrobbling."
    }
)
