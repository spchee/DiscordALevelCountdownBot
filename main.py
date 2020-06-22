import os
import discord
from discord.ext import commands
import datetime
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    print("bot is ready")

@client.command()
async def countdown(ctx):

    time = datetime.datetime(2020, 8, 13,7,30) - datetime.datetime.now()
    days = time.days
    hours = time.seconds//3600
    minutes = (time.seconds%3600)//60
    embed=discord.Embed(title="Time left until A-level Results", color=0xe32323)
    embed.add_field(name="Days", value=days, inline=True)
    embed.add_field(name="Hours", value=hours, inline=True)
    embed.add_field(name="Minutes", value=minutes, inline=True)
    embed.set_footer(text="A-Level Coutndown Bot")
    await ctx.send(embed = embed)

token = "CHANGE TOKEN"
client.run(token)
