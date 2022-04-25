import random
import os

import discord
from discord.ext import commands

from dow_bot.settings import BOT_TOKEN

from dow_bot.settings import URL_PIC

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'unloaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'reloaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(BOT_TOKEN)
