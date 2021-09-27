# import discord
from discord.ext import commands
from asyncio import sleep as s
from datetime import datetime
import os

# client = discord.Client()
bot = commands.Bot(command_prefix = "!")

"""
@client.event
async def on_ready():
    print("Dynamic Bot is now online.")
"""

@bot.command()
async def desc(ctx):
    await ctx.send("Hey there! I am a Dynamic Bot. If you wanna set a reminder, Dynamic Bot is there for you!\nPeace!!✌")

@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

@bot.command()
async def time(ctx):
    x = datetime.now()
    local = x.astimezone()
    local_tz = local.tzinfo
    local_2 = local_tz.tzname(local)
    await ctx.send(x)
    await ctx.send(local_2)

@bot.command()
async def reminder(ctx, time: str, *, msg):
    li = list(map(int, time.split(":")))
    current = datetime.now()
    hour = int(current.strftime("%H"))
    minute = int(current.strftime("%M"))

    hour = li[0] - hour
    minute = li[1] - minute

    time = (hour * 3600) + (minute * 60)
    print(time)

    while True:
        await s(time)
        await ctx.send(f'Buckle up @everyone! {msg} is coming up!! Be prepared...')
        break

#bot.run(os.environ["TOKEN"])
bot.run("ODkxNzYyOTcyNzM5OTE1ODc3.YVDE_A.4kQ28CqeJ_9j0csDiatee9Mupo4")
#client.run(token)