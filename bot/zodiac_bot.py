import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
load_dotenv()

bot = commands.Bot(command_prefix='!')

async def on_ready():
    print('Bot is online')

bot.run(os.getenv('TOKEN'))