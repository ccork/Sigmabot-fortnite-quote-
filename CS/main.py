from discord.ext import commands
import discord
import random

BOT_TOKEN = "ADD TOKEN HERE"
CHANNEL_ID = ADD CHANNEL ID HERE

# Define your intents
intents = discord.Intents.all()

# Initialize the bot with intents
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f'sigma meal skibidi slicers ({bot.user} online)')
    await channel.send('`use ?forgnite`')
@bot.command()
async def forgnite(ctx):
    # Open the text file containing the strings
    with open('Lists.txt', 'r') as file:
        # Read all the lines from the file
        lines = file.readlines()
    
    # Choose a random string from the list of lines
    random_string = random.choice(lines)
    
    # Send the random string as a message
    await ctx.send(random_string)

@bot.command()
async def helpme(ctx):
    await ctx.send('Use the `?forgnite` command to get the fortnite quote of the day,')

@bot.command()
async def todo(ctx):
    await ctx.send("**TODO**")
    await ctx.send("`--Host the bot so it's on 24/7`")
    await ctx.send("`--Self-Configurable channel location`")
    await ctx.send("`--Multiple instances for multiple servers`")

bot.run(BOT_TOKEN)
    