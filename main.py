from discord.ext import commands
from discord import Embed, Color, Status
from dotenv import load_dotenv
import os

load_dotenv()

#Setting the Syntax
bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'))


token = os.getenv('TOKEN')

bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=Status.idle)

#List of Cogs
extensions = ['cmds.Commands']

#initiation of Cogs
for cogs in extensions:
    bot.load_extension(f'{cogs}')

bot.run(token)
