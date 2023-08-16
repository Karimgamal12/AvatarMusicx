#
# Copyright (C) 2021-2022 by TeamAvatar @Github, < https://github.com/TeamAvatar  >.
#
# This file is part of < https://github.com/TeamAvatar /Avatar MusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamAvatar /Avatar MusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Avatar Music import LOGGER, app, userbot
from Avatar Music.core.call import Avatar 
from Avatar Music.plugins import ALL_MODULES
from Avatar Music.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Avatar Music").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Avatar Music").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Avatar Music.plugins" + all_module)
    LOGGER("Avatar music.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Avatar .start()

    await Avatar .decorators()
    LOGGER("Avatar Music").info("Avatar  Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Avatar Music").info("Stopping Avatar  Music Bot! GoodBye")
