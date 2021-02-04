import discord
import time
import asyncio
from discord.ext import commands, tasks

OWNERS = []
CHANNEL_IDS = []
channelId = 123456789 #for notification

Monday = {(9, 40):"```Sub lec. is about to start```",
           (10, 40):"```Sub2 lec. will begin shortly```",
           (11, 40):"```Sub3 lec. will begin shortly```",
           (13, 25):"```Sub4 lec. will begin shortly```",
           (14, 25):"```Sub5 (PR) will begin shortly```"}

Tuesday = {(9, 40):"```Sub5 lec. is about to start```",
           (11, 40):"```Sub2 lec. will begin shortly```",
           (13, 25):"```Sub4 lec. will begin shortly```",
           (14, 25):"```Sub3 (PR) will begin shortly```"}


Wednesday = {(9, 40):"```Sub lec. is about to start```",
           (10, 40):"```Sub4 lec. will begin shortly```",
           (11, 40):"```Sub3 lec. will begin shortly```",
           (13, 25):"```Sub5 (PR) will begin shortly```",
           (14, 25):"```Sub4 (PR) will begin shortly```"}

Thursday = {(9, 40):"```Sub3 lec. is about to start```",
           (10, 40):"```Sub2 lec. will begin shortly```",
           (11, 40):"```Sub5 lec. will begin shortly```",
           (13, 25):"```Sub lec. will begin shortly```",
           (14, 25):"```Sub2 (PR) will begin shortly```"}

Friday = {(9, 40):"```Sub2 lec. is about to start```",
           (10, 40):"```Sub lec. will begin shortly```",
           (11, 40):"```Sub3 lec. will begin shortly```",
           (14, 25):"```Sub (PR) will begin shortly```"}

class DailyTask(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.task.start()


    @tasks.loop()
    async def task(self):
        await self.client.wait_until_ready()
        channel = self.client.get_channel(channelId)        
        cTime = tuple([int(i) for i in time.ctime().split()[3].split(":")[:2]])
        day = time.ctime().split()[0]
        message = "<@&1234>\n" + "{}" #replace 1234 with you role id, this will mention role while sending message
        if day == "Mon":
            if cTime in Monday:
                await channel.send(message.replace("{}", Monday[cTime]))
                await asyncio.sleep(60)
        elif day == "Tue":
            if cTime in Tuesday:
                await channel.send(message.replace("{}", Tuesday[cTime]))
                await asyncio.sleep(60)
        elif day == "Wed":
            if cTime in Wednesday:
                await channel.send(message.replace("{}", Wednesday[cTime]))
                await asyncio.sleep(60)
        elif day == "Thu":
            if cTime in Thursday:
                await channel.send(message.replace("{}", Thursday[cTime]))
                await asyncio.sleep(60)
        elif day == "Fri":
            if cTime in Friday:
                await channel.send(message.replace("{}", Friday[cTime]))
                await asyncio.sleep(60)
        await asyncio.sleep(1)

# To turn on or off task

    @commands.command()
    async def start(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
            return False
        elif ctx.message.author.id in OWNERS:
            self.task.start()
            await ctx.message.channel.send(f"Starting Task... 🟢")
        else:
            await ctx.message.channel.send("You don't have permission to use this command")

    @commands.command()
    async def stop(self, ctx):
        if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
            await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
            return False
        elif ctx.message.author.id in OWNERS:
            self.task.stop()
            await ctx.message.channel.send(f"Stopping Task... 🛑")
        elif ctx.message.author.id in OWNERS:
            await ctx.message.channel.send(f"Task is already stopped...")
        else:
            await ctx.message.channel.send("You don't have permission to use this command")


def setup(client):
    client.add_cog(DailyTask(client))
