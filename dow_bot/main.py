import random

import discord
from discord.ext import commands

from dow_bot.settings import BOT_TOKEN
from dow_bot.settings import TEST_CHANNEL_ID
from dow_bot.settings import URL_PIC

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(TEST_CHANNEL_ID))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f"{member} leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)} (ms)')

# @bot.command()
# async def picture(ctx):
#     pic = discord.File()
#     await ctx.send(file=pic)

@bot.command()
async def picture(ctx):
    await ctx.send(URL_PIC)

bot.run(BOT_TOKEN)
