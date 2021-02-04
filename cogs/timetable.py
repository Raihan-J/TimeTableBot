import discord
import time
from discord.ext import commands


CHANNEL_IDS=[]

class Timetable(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def mon(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            author = ctx.author.mention
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.set_author(name="Monday's timetable")
            embed.add_field(name="1. sub1",value="by ", inline=False)
            embed.add_field(name="2. sub2",value="by ", inline=False)
            embed.add_field(name="3. sub3",value="by ", inline=False)
            embed.add_field(name="4. sub4",value="by ", inline=False)
            embed.add_field(name="5. sub5",value="by ", inline=False)
            await ctx.send(author, embed=embed)

    @commands.command()
    async def tue(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            author = ctx.author.mention
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.set_author(name="Tuesday's timetable")
            embed.add_field(name="1. sub1",value="by ", inline=False)
            embed.add_field(name="2. sub2",value="by ", inline=False)
            embed.add_field(name="3. sub3",value="by ", inline=False)
            embed.add_field(name="4. sub4",value="by ", inline=False)
            embed.add_field(name="5. sub5",value="by ", inline=False)
            await ctx.send(author, embed=embed)

    @commands.command()
    async def wed(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            author = ctx.author.mention
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.set_author(name="Wednesday's timetable")
            embed.add_field(name="1. sub1",value="by ", inline=False)
            embed.add_field(name="2. sub2",value="by ", inline=False)
            embed.add_field(name="3. sub3",value="by ", inline=False)
            embed.add_field(name="4. sub4",value="by ", inline=False)
            embed.add_field(name="5. sub5",value="by ", inline=False)
            await ctx.send(author, embed=embed)

    @commands.command()
    async def thu(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            author = ctx.author.mention
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.set_author(name="Thursday's timetable")
            embed.add_field(name="1. sub1",value="by ", inline=False)
            embed.add_field(name="2. sub2",value="by ", inline=False)
            embed.add_field(name="3. sub3",value="by ", inline=False)
            embed.add_field(name="4. sub4",value="by ", inline=False)
            embed.add_field(name="5. sub5",value="by ", inline=False)
            await ctx.send(author, embed=embed)

    @commands.command()
    async def fri(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            author = ctx.author.mention
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.set_author(name="Friday's timetable")
            embed.add_field(name="1. sub1",value="by ", inline=False)
            embed.add_field(name="2. sub2",value="by ", inline=False)
            embed.add_field(name="3. sub3",value="by ", inline=False)
            embed.add_field(name="4. sub4",value="by ", inline=False)
            embed.add_field(name="5. sub5",value="by ", inline=False)
            await ctx.send(author, embed=embed)

    @commands.command()
    async def sat(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            await ctx.send(f"{ctx.author.mention}\nGo back to sleep, it's Saturday")

    @commands.command()
    async def sun(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            await ctx.send(f"{ctx.author.mention}\nGo back to sleep, it's Sunday")

def setup(client):
    client.add_cog(Timetable(client))