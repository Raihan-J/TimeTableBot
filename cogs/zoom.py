import discord
import time
from discord.ext import commands


CHANNEL_IDS=[]

class Zoom(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def sub(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            await ctx.send(f"{ctx.author.mention}\nSubject (sub) by : https://zoom.us/")

    @commands.command()
    async def sub2(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            await ctx.send(f"{ctx.author.mention}\nsSubject (sub) by : https://zoom.us/")

    @commands.command()
    async def sub3(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            await ctx.send(f"{ctx.author.mention}\nSubject (sub) by : https://zoom.us/")

    @commands.command()
    async def sub4(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            await ctx.send(f"{ctx.author.mention}\nSubject (sub) by : https://zoom.us/")

    @commands.command()
    async def sub5(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            await ctx.send(f"{ctx.author.mention}\nSubject (sub) by : https://zoom.us/")

    @commands.command()
    async def sub6(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            await ctx.send(f"{ctx.author.mention}\nSubject (sub) by : https://zoom.us/")

    @commands.command()
    async def subpr(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            await ctx.send(f"{ctx.author.mention}\nSubject (sub) by : https://zoom.us/")

    @commands.command()
    async def sub2pr(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            await ctx.send(f"{ctx.author.mention}\nSubject (sub) by : https://zoom.us/")

def setup(client):
    client.add_cog(Zoom(client))