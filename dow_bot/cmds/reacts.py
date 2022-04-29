from random import randint
import discord
from discord.ext import commands

from dow_bot.core.classes import Cog_Extension
from dow_bot.settings import URL_PIC

class React(Cog_Extension):

    # @commands.command()
    # async def picture(ctx):
    #     pic = discord.File()
    #     await ctx.send(file=pic)

    @commands.command()
    async def picture(self, ctx):
        await ctx.send('none')


def setup(bot):
    bot.add_cog(React(bot))