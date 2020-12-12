#!/usr/bin/env python3
"bot.py"
import logging

import discord
from discord.ext import commands

logger = logging.getLogger(__name__)
bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    "Logs connection attempt and guild id on sucessful login"

    if len(bot.guilds) > 2:
        print("We've been hacked!")
        bot.close()
    for guild in bot.guilds:
        logger.info(
            "%s is connected to the following guild: %s: (id: %s)", bot.user.name, guild.name, guild.id
        )
