import discord
import time
import asyncio
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

status = cycle(['Making Your Life Easy!!', 'Listening to .help'])

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready...')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.author.mention

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name="Command's you can use...")
    embed.add_field(name='.ping',value='Pings the bot', inline=False)
    embed.add_field(name='.hello',value="let's find out...", inline=False)
    embed.add_field(name='.dce', value='Display the subject zoom link',inline=False)
    embed.add_field(name='.tv', value='Display the subject zoom link',inline=False)
    embed.add_field(name='.dtsp', value='Display the subject zoom link',inline=False)
    embed.add_field(name='dc', value='Display the subject zoom link',inline=False)
    embed.add_field(name='.ee', value='Display the subject zoom link',inline=False)
    embed.add_field(name='.mpi', value='Display the subject zoom link',inline=False)
    embed.add_field(name='.bce', value='Display the subject zoom link',inline=False)    
    embed.add_field(name='.dcpr', value='Display the practical zoom link',inline=False)
    embed.add_field(name='.ostcpr', value='Display the practical zoom link',inline=False)
    embed.add_field(name='.dcepr', value='Display the practical zoom link',inline=False)
    embed.add_field(name='.tvpr', value='Display the practical zoom link',inline=False)
    embed.add_field(name='.mpipr', value='Display the practical zoom link',inline=False)
    embed.add_field(name='.monday', value="Display monday's timetable",inline=False)
    embed.add_field(name='.tuesday', value="Display tuesday's timetable",inline=False)
    embed.add_field(name='.wednesday', value="Display wednesday's timetable",inline=False)
    embed.add_field(name='.thursday', value="Display thursday's timetable",inline=False)
    embed.add_field(name='.friday', value="Display friday's timetable",inline=False)
    embed.add_field(name='.help', value='Display the help command duh.', inline=False)
    await ctx.send(author, embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f"{ctx.author.mention}\nPing! {round(client.latency * 1000)}ms")

@client.command()
async def hello(ctx):
    await ctx.send(f'hey!! {ctx.author.mention}')

@client.command()
async def dce(ctx):
    await ctx.send(f"{ctx.author.mention}\nData Compression And Encryption (DCE) by Teachers name : https://zoom.us/")

@client.command()
async def tv(ctx):
    await ctx.send(f"{ctx.author.mention}\nTV & Video Engineering (TV) by Teachers name : https://zoom.us/")

@client.command()
async def dtsp(ctx):
    await ctx.send(f"{ctx.author.mention}\nDiscrete Time Signal Processing (DTSP) by Teachers name : https://zoom.us/")

@client.command()
async def dc(ctx):
    await ctx.send(f"{ctx.author.mention}\nDigital Communication (DC) by Teachers name : https://zoom.us/")

@client.command()
async def ee(ctx):
    await ctx.send(f"{ctx.author.mention}\nElectromagnetic Engineering (EE) by Teachers name : https://zoom.us/")

@client.command()
async def bce(ctx):
    await ctx.send(f"{ctx.author.mention}\nBusiness Communication Ethics (BCE) by Teachers name : https://zoom.us/")

@client.command()
async def mpi(ctx):
    await ctx.send(f"{ctx.author.mention}\nMicroprocessor & Peripherals Interfacing (MPI) by Teachers name : https://zoom.us/")

@client.command()
async def dcepr(ctx):
    await ctx.send(f"{ctx.author.mention}\nData Compression And Encryption (DCE) by Teachers name : https://zoom.us/")

@client.command()
async def tvpr(ctx):
    await ctx.send(f"{ctx.author.mention}\nTV & Video Engineering (TV) by Teachers name : https://zoom.us/")

@client.command()
async def ostcpr(ctx):
    await ctx.send(f"{ctx.author.mention}\nOpen Source Technology for Communication (OSTC) Teachers name : https://zoom.us/")

@client.command()
async def mpipr(ctx):
    await ctx.send(f"{ctx.author.mention}\nMicroprocessor & Peripherals Interfacing (MPI) Teachers name : https://zoom.us/")

@client.command()
async def dcpr(ctx):
    await ctx.send(f"{ctx.author.mention}\nDigital Communication (DC) by Teachers name : https://zoom.us/")

@client.command(pass_context=True)
async def monday(ctx):
    author = ctx.author.mention

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name="Monday's timetable")
    embed.add_field(name="1. DCE / TV",value="by Teachers name", inline=False)
    embed.add_field(name="2. DTSP",value="by Teachers name", inline=False)
    embed.add_field(name="3. DTSP",value="by Teachers name", inline=False)
    embed.add_field(name="4. DC (PR)",value="by Teachers name", inline=False)
    await ctx.send(author, embed=embed)

@client.command()
async def tuesday(ctx):
    author = ctx.author.mention

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name="Tuesday's timetable")
    embed.add_field(name="1. EE",value="by Teachers name", inline=False)
    embed.add_field(name="2. EE",value="by Teachers name", inline=False)
    embed.add_field(name="3. DC",value="by Teachers name", inline=False)
    embed.add_field(name="4. OSTC (PR)",value="by Teachers name", inline=False)
    await ctx.send(author, embed=embed)

@client.command()
async def wednesday(ctx):
    author = ctx.author.mention

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name="Wednesday's timetable")
    embed.add_field(name="1. DCE / TV",value="by Teachers name", inline=False)
    embed.add_field(name="2. BCE",value="by Teachers name", inline=False)
    embed.add_field(name="3. MPI",value="by Teachers name", inline=False)
    embed.add_field(name="4. DCE / TV (PR)",value="by Teachers name", inline=False)
    await ctx.send(author, embed=embed)

@client.command()
async def thursday(ctx):
    author = ctx.author.mention

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name="Thursday's timetable")
    embed.add_field(name="1. MPI",value="by Teachers name", inline=False)
    embed.add_field(name="2. EE",value="by Teachers name", inline=False)
    embed.add_field(name="3. DCE / TV",value="by Teachers name", inline=False)
    embed.add_field(name="4. MPI (PR)",value="by Teachers name", inline=False)
    embed.add_field(name="5. MPI",value="by Teachers name", inline=False)
    await ctx.send(author, embed=embed)

@client.command()
async def friday(ctx):
    author = ctx.author.mention

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name="Friday's timetable")
    embed.add_field(name="1. EE",value="by Teachers name", inline=False)
    embed.add_field(name="2. MPI",value="by Teachers name", inline=False)
    embed.add_field(name="3. DC",value="by Teachers name", inline=False)
    await ctx.send(author, embed=embed)

@client.command()
async def saturday(ctx):
    await ctx.send(f"{ctx.author.mention}\nGo back to sleep, it's Saturday")

@client.command()
async def sunday(ctx):
    await ctx.send(f"{ctx.author.mention}\nGo back to sleep, it's Sunday")


Monday = {(9, 55):"``DCE / TV lec. is about to start``",
           (10, 55):"``DTSP lec. will begin shortly``",
           (13, 55):"``DC (PR) will begin shortly``"}

Tuesday = {(9, 55):"``EE lec. is about to start ``",
           (11, 55):"``DC lec. will begin shortly``",
           (13, 55):"``OSTC (PR) will begin shortly``"}


Wednesday = {(9, 55):"``DCE / TV lec. is about to start ``",
           (10, 55):"``BCE lec. will begin shortly``",
           (11, 55):"``MPI lec. will begin shortly``",
           (13, 55):"``DCE /TV (PR) will begin shortly``"}

Thursday = {(9, 55):"``MPI lec. is about to start ``",
           (10, 55):"``EE lec. will begin shortly``",
           (11, 55):"``DCE / TV lec. will begin shortly``",
           (13, 55):"``MPI (PR) will begin shortly``",
           (14, 55):"``MPI lec. will begin shortly``"}

Friday = {(9, 55):"``EE is about to start ``",
           (10, 55):"``MPI will begin shortly``",
           (11, 55):"``DC will begin shortly``"}

channelId = 123456789       # Channel id where to send notification  

async def task():
    await client.wait_until_ready()
    channel = client.get_channel(channelId)
    while client.is_closed:
        
        cTime = tuple([int(i) for i in time.ctime().split()[3].split(":")[:2]])
        day = time.ctime().split()[0]
        message = "<@&12345>\n" + "{}" # replace 12345 with your role id this will mention roles when sending message
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
client.loop.create_task(task())

client.run('TOKEN') # put your token here