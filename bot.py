#!/usr/bin/env python3
"bot.py"
import auth
import argparse
import discord
import logging

LOG_LOC = "./qbot.log"
TOKEN = auth.DISCORD_TOKEN
GUILD = auth.DISCORD_GUILD


client = discord.Client()


def setup_arguments():
    """
    Sets up command line arguments to allow for debug and optional log file
    location
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d",
        "--debug", 
        action="store_true", 
        help="Sets debug mode"
        ) 
    parser.add_argument(
        "-f",
        "--filename",
        action="store",
        type=str,
        default=LOG_LOC,
        help="Location where the log file will be located"
        )
    return parser.parse_args()


def setup_logging(debug, file_name):
    """
    Sets defaults for logging
    """
    log_format = '%(asctime)s - %(message)s'
    if debug:
        severity = logging.DEBUG
    else:
        severity = logging.INFO
    logging.basicConfig(format=log_format, level=severity, filename=file_name)
     



@client.event
async def on_ready():
    """
    Logs connection attempt and guild id on sucessful login
    """
    if len(client.guilds) > 1:
        print("We've been hacked")
        client.close()
    guild = discord.utils.get(client.guilds,name=GUILD)
    logging.info(
        "%s is connected to the following guild: \
%s: (id: %s)", client.user, guild.name, guild.id
        )


if __name__  == "__main__":    
    args = setup_arguments()
    setup_logging(args.debug, args.filename)
    client.run(TOKEN)
 
