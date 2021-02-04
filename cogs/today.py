import discord
import time
from discord.ext import commands
from datetime import datetime

CHANNEL_IDS=[]

class Today(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def td(self, ctx):
        days = datetime.today().weekday()
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        else:
            if days == 0:
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

            elif days == 1:
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
            
            elif days == 2:
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

            elif days == 3:
                author = ctx.author.mention
                embed = discord.Embed(
                    colour = discord.Colour.blue()
                )
                embed.add_field(name="1. sub1",value="by ", inline=False)
                embed.add_field(name="2. sub2",value="by ", inline=False)
                embed.add_field(name="3. sub3",value="by ", inline=False)
                embed.add_field(name="4. sub4",value="by ", inline=False)
                embed.add_field(name="5. sub5",value="by ", inline=False)
                await ctx.send(author, embed=embed)

            elif days == 4:
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

            elif days == 5:
                await ctx.send(f"{ctx.author.mention}\nGo back to sleep, it's Saturday")

            elif days == 6:
                await ctx.send(f"{ctx.author.mention}\nGo back to sleep, it's Sunday")
            else:
                await ctx.send('Getting error..... <@owner_id>')

def setup(client):
    client.add_cog(Today(client))