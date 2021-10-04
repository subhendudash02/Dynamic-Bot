# import discord
from discord.ext import commands
from asyncio import sleep as s
from datetime import datetime
import time as tt
import os
import pytz

# client = discord.Client()
bot = commands.Bot(command_prefix = "!")

region = pytz.timezone("Asia/Kolkata")

"""
@client.event
async def on_ready():
    print("Dynamic Bot is now online.")
"""

@bot.command()
async def desc(ctx):
    await ctx.send("Hey there! I am a Dynamic Bot. If you wanna set a reminder, Dynamic Bot is there for you!\nPeace!!✌")

"""
bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
"""

@bot.command()
async def time(ctx):
    TIME = datetime.now(region)
    await ctx.send(f"Hey, {ctx.guild}! The time is {}")

@bot.command()
async def reminder(ctx, date: str,Time: str, *, msg):
    time_format = "%d/%m/%Y %H:%M"
    upcoming_time = date + " " + Time
    Now = datetime.now(region)
    current_time = Now.strftime(time_format)

    d1 = datetime.strptime(current_time, time_format)
    d2 = datetime.strptime(upcoming_time, time_format)

    d1 = tt.mktime(d1.timetuple())
    d2 = tt.mktime(d2.timetuple())

    print(d2 - d1)   # To check the seconds

    while True:
        await s(d2 - d1)
        await ctx.send(f'Buckle up @everyone! {msg} is coming up!! Be prepared...')
        break

#bot.run(os.environ["TOKEN"])
#client.run(token)