import discord
from discord.ext import commands

from dow_bot.core.classes import Cog_Extension
from dow_bot.settings import TEST_CHANNEL_ID


class Events(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(TEST_CHANNEL_ID))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} leave!")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'apple':
            await msg.channel.send('hi')

def setup(bot):
    bot.add_cog(Events(bot))
