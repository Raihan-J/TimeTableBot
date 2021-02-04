import discord
import time
import asyncio
from discord.ext import commands

OWNERS = []
CHANNEL_IDS=[]

class Maintenance(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def s(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
            return False
        elif ctx.message.author.id in OWNERS:
            await ctx.message.channel.send(f"Going to sleep.. 😴")
        else:
            await ctx.message.channel.send("You don't have permission to use this command")

    @commands.command(pass_context=True)
    async def o(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
            return False
        elif ctx.message.author.id in OWNERS:
            await ctx.message.channel.send(f"Back Online.. 🥳")
        else:
            await ctx.message.channel.send("You don't have permission to use this command")
            
def setup(client):
    client.add_cog(Maintenance(client))