import discord
from discord.ext import commands

from dow_bot.settings import BOT_TOKEN

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(965637244377497620)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f"{member} leave!")

bot.run(BOT_TOKEN)