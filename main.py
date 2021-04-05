import discord
import os
import asyncio
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')

status = cycle(['.h', '... year routine'])

client.remove_command('help')

OWNERS = []
CHANNEL_IDS = []

@client.event
async def on_ready():
    change_status.start()
    print('BoT is online...')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid Command...')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=2, name=next(status)))

@client.command()
async def load(ctx, extension):
    if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
        await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        return False
    elif ctx.message.author.id in OWNERS:
        client.load_extension(f'cogs.{extension}')
        await ctx.message.channel.send(f'Successfully Loaded..')
    else:
        await ctx.message.channel.send("You don't have permission to use this command")

@client.command()
async def unload(ctx, extension):
    if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
        await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        return False
    elif ctx.message.author.id in OWNERS:
        client.unload_extension(f'cogs.{extension}')
        await ctx.message.channel.send(f'Successfully Unloaded..')
    else:
        await ctx.message.channel.send("You don't have permission to use this command")

@client.command()
async def reload(ctx, extension):
    if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
        await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
        return False
    elif ctx.message.author.id in OWNERS:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.message.channel.send(f'Successfully Reloaded.. 🔄')
    else:
        await ctx.message.channel.send("You don't have permission to use this command")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.group(name='h', invoke_without_command=True)
async def helpcommand(ctx):
    if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
        await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
    else:
        author = ctx.author.mention
        embed = discord.Embed(
            colour = discord.Colour.blue()
        )

        embed.set_author(name="Command's you can use...")
        embed.add_field(name='.ping',value='Pings the bot', inline=False)
        embed.add_field(name='.hello',value="BoT says hey!!", inline=False)
        embed.add_field(name='.td', value="Display today's timetable",inline=False)
        embed.add_field(name='.h zoom', value="Display command's to view zoom link",inline=False)
        embed.add_field(name='.h tt', value="Display command's to view timetable",inline=False)
        await ctx.send(author, embed=embed)

@helpcommand.command(name='zoom')
async def zoom_subcommand(ctx):
    if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
        await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
    else:
        author = ctx.author.mention
        embed = discord.Embed(
            colour = discord.Colour.blue()
        )
        embed.set_author(name="Command's to view zoom link")
        embed.add_field(name='.sub', value='Display the subject zoom link',inline=False)
        embed.add_field(name='.sub2', value='Display the subject zoom link',inline=False)
        embed.add_field(name='.sub3', value='Display the subject zoom link',inline=False)
        await ctx.send(author, embed=embed)

@helpcommand.command(name='tt')
async def timetable_subcommand(ctx):
    if len(CHANNEL_IDS) > 0 and ctx.message.channel.id not in CHANNEL_IDS:
        await ctx.message.channel.send(f"{ctx.author.mention}\nI don't respond to commands in this channel. Go to <#channel_id>",delete_after=10)
    else:
        author = ctx.author.mention
        embed = discord.Embed(
            colour = discord.Colour.blue()
        )
        embed.set_author(name="Command's to view timetable day vise.")
        embed.add_field(name='.mon', value="Display monday's timetable",inline=False)
        embed.add_field(name='.tue', value="Display tuesday's timetable",inline=False)
        embed.add_field(name='.wed', value="Display wednesday's timetable",inline=False)
        embed.add_field(name='.thu', value="Display thursday's timetable",inline=False)
        embed.add_field(name='.fri', value="Display friday's timetable",inline=False)
        await ctx.send(author, embed=embed)

client.run('')#TOKEN
