# import discord
from discord.ext import commands
from asyncio import sleep as s
from datetime import datetime
import time as tt
import os
import pytz
import nacl

# client = discord.Client()
bot = commands.Bot(command_prefix = "!")

# bot.remove_command("help")

region = pytz.timezone("Asia/Kolkata")

"""
@client.event
async def on_ready():
    print("Dynamic Bot is now online.")
"""

@bot.command(name='desc', help='About Me 😁')
async def desc(ctx):
    await ctx.send("Hey there! I am a Dynamic Bot. If you wanna set a reminder, Dynamic Bot is there for you!\nPeace!!✌")

# @bot.command()
# async def help(ctx):
#     await ctx.send("**Commands by Dynamic-Bot: ** \n")
#     await ctx.send("1. `!desc` : About Me 😁 \n")
#     await ctx.send("2. `!time` : Ask the current time \n")
#     await ctx.send("3. `!reminder <date: dd/mm/yyyy> <time: hh:mm> <event_name>` : Set a reminder of any Event \n")
#     await ctx.send("4. `!join` : Join the discord server (make sure you join first) \n")
#     await ctx.send("5. `!leave` : Leave the discord server")

"""
bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
"""

@bot.command(name='!time', help='Ask the current time')
async def time(ctx):
    TIME = datetime.now(region)
    x = TIME.strftime("%H:%M:%S")
    await ctx.send(f"Hey, {ctx.author}! The time is {x}")

@bot.command(name='!reminder', help='Format: `<date: dd/mm/yyyy> <time: hh:mm> <event_name>`')
async def reminder(ctx, date: str,Time: str, *, msg):
    time_format = "%d/%m/%Y %H:%M"
    upcoming_time = date + " " + Time
    Now = datetime.now(region)
    current_time = Now.strftime(time_format)

    d1 = datetime.strptime(current_time, time_format)
    d2 = datetime.strptime(upcoming_time, time_format)

    d1 = tt.mktime(d1.timetuple())
    d2 = tt.mktime(d2.timetuple())

    print("Time left: ", d2 - d1)   # To check the seconds

    while True:
        await s(d2 - d1)
        await ctx.send(f'Buckle up @everyone! {msg} is coming up!! Be prepared...')
        break

@bot.command(name='!join', help='Join the discord server (make sure you join first)')
async def join(ctx):
    vc = ctx.author.voice

    if ctx.author.voice == None:
        await ctx.send(f'@everyone The voice-channel is empty. Kindly join the voice-channel then type the command again.')
    else:
        await ctx.send("Joined!!!")
        await vc.channel.connect()

@bot.command(name='!leave', help='Leave the discord server')
async def leave(ctx):
    vc_leave = ctx.voice_client
    await vc_leave.disconnect()
    await ctx.send("Left!!!")

bot.run(os.environ["TOKEN"])
