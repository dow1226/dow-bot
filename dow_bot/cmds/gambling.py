import random
import asyncio

from discord.ext import commands

from dow_bot.core.classes import Cog_Extension
from dow_bot.core.economy import Economy


class Gambling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.economy = Economy()

    @commands.command()
    async def dice(self, ctx, choice:int, bet:int):
        await ctx.send('開骰')
        asyncio.sleep(3)
        roll_dice = random.randint(1, 6)
        await ctx.send(f'骰出{roll_dice}點!')
        choices = range(1, 7)
        if choice in choices:
            if choice == roll_dice:
                await ctx.send(f'{ctx.author} 賭中啦! 贏得{bet * 5}元!')
                self.economy.add_money(ctx.author.id, bet * 5)
            else:
                await ctx.send(f'{ctx.author} 沒中! 輸了{bet}元!')
                self.economy.add_money(ctx.author.id, bet * -1)
        else:
            raise Exception



def setup(bot):
    bot.add_cog(Gambling(bot))
