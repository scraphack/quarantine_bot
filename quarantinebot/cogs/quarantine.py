#!/usr/bin/env python3
from discord.ext import commands
from datetime import datetime as dt

class Quarantine(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._q_start = "05/11/2020 00:01:00"


    @staticmethod
    def get_lock_time(date_start):
        """
        Takes in a datetime object and returns the time since that date in 
        days hours and minutes.
        """
        date_now = dt.now()
        delta = date_now - date_start
        delta_days = delta.days
        delta_secs = delta.seconds
        delta_mins = delta_secs / 60
        delta_hours = delta_mins / 60
        lock_hours = int(delta_hours)
        lock_mins = int(delta_mins - (lock_hours * 60))
        return delta_days, lock_hours, lock_mins
     
    @commands.command()
    async def lockdown(self, ctx):
        "Returns time since lockdown started"
        start_obj = dt.strptime(self._q_start, "%d/%m/%Y %H:%M:%S")
        start_text = start_obj.strftime("%H:%M:%S on %A %d %B %Y")
        lock_days, lock_hours, lock_mins = self.get_lock_time(start_obj)
        response_text = f"""```Hi {ctx.author}!

You have been in lockdown for:

    {lock_days} days, {lock_hours} hours and {lock_mins} minutes.

This timer is counting up from the announcement of a UK wide \
lockdown at {start_text}```"""
        await ctx.send(response_text)
