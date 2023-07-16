import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(intents=discord.Intents.all() , command_prefix='/' , description='The Best Music-Bot For the Best User!')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
@bot.event
async def on_ready():
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))

bot.run(TOKEN)