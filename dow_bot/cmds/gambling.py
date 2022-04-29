import random
import time
import json

from discord.ext import commands

from dow_bot.core.classes import Cog_Extension



class Gambling(Cog_Extension):

    @commands.command()
    async def dice(self, ctx):
        await ctx.send('賭骰開始! /n 下注方式 !bet {號碼} {金額}')

    @commands.command()
    async def bet(self, ctx, choice:int, money:int):
        player_name = str(ctx.author)
        choices = choice
        bet = money
        player_dict = {player_name: {"choice": choices, "bet": bet}}

        with open("game.json", "w") as jsfile:
            json.dump(player_dict, jsfile)

        await ctx.send(f'{player_name} 賭開{choices} {bet}元')

    @commands.command()
    async def 封盤(self, ctx):
        await ctx.send('封盤!')
        result = random.randint(1, 6)
        await ctx.send(f'開出{result}點!')
        with open("game.json", "r") as jsfile:
            game_dict = json.load(jsfile)
        for k in game_dict.keys():
            choice = game_dict[k]['choice']
            bet = game_dict[k]['bet']
            if choice == result:
                await ctx.send(f'{k}贏得了{bet}元')
            else:
                await ctx.send(f'{k}輸了{bet}元')
        with open("game.json", "w") as jsfile:
            jsfile.seek(0)
            jsfile.truncate()

    # @commands.command()
    # async def dice(self, ctx, choice:int, bet:int):
    #     await ctx.send('開骰')
    #     time.sleep(3)
    #     roll_dice = random.randint(1, 6)
    #     await ctx.send(f'骰出{roll_dice}點!')
    #     choices = range(1, 7)
    #     if choice in choices:
    #         if choice == roll_dice:
    #             await ctx.send(f'{ctx.author} 賭中啦! 贏得{bet * 5}元!')
    #             self.economy.add_money(ctx.author.id, bet * 5)
    #         else:
    #             await ctx.send(f'{ctx.author} 沒中! 輸了{bet}元!')
    #             self.economy.add_money(ctx.author.id, bet * -1)
    #     else:
    #         raise Exception


def setup(bot):
    bot.add_cog(Gambling(bot))
