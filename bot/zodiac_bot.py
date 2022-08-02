import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
load_dotenv()

bot = commands.Bot(command_prefix='!')

async def on_ready():
    print('Bot is online')

@bot.command()
async def hello(ctx):
    if (str(ctx.author) == "walt#9586"):
        return
    await ctx.channel.send(f'Hello {ctx.author.mention}!')

@bot.command()
async def goodbye(ctx):
    if (str(ctx.author) == "walt#9586"):
        return
    await ctx.channel.send(f'Goodbye {ctx.author.mention}!')

bot.run(os.getenv('TOKEN'))