#!/usr/bin/env python3
"bot.py"
import logging

import discord
from discord.ext import commands

import quarantinebot.auth as auth
import quarantinebot.cogs as cogs

TOKEN = auth.DISCORD_TOKEN
GUILD = auth.DISCORD_GUILD

logger = logging.getLogger(__name__)
bot = commands.Bot(command_prefix='$')
bot.add_cog(cogs.Quarantine(bot))

@bot.event
async def on_ready():
    "Logs connection attempt and guild id on sucessful login"

    if len(bot.guilds) > 2:
        print("We've been hacked")
        bot.close()
    guild = discord.utils.get(bot.guilds,name=GUILD)
    logger.info(
        "%s is connected to the following guild: \
%s: (id: %s)", bot.user.name, guild.name, guild.id
        )

