import discord
from discord.ext import commands
import json
import asyncio
import datetime

from dow_bot.core.classes import Cog_Extension


class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def setup(bot):
    bot.add_cog(Task(bot))