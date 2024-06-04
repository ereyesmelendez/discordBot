import datetime
from discord.ext import commands 
import discord
from dataclasses import dataclass

BOT_TOKEN = #"enter your token ID here"
CHANNEL_ID = #enter your channel ID here, #id needs to be a number and not a string for the bot to understand

@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix= "!", intents = discord.Intents.all())
session = Session()

@bot.event
async def on_ready():
    print("Hello! Bot has been booted up from Skynet.")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Bot has been booted up from Skynet.")
    
@bot.command()
async def start(ctx):
    if session.is_active:
        await ctx.send("A session is already active!")
        return
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")
    await ctx.send(f"Session started at {human_readable_time}")

@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("No active session!")
        return

    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    human_readable_duration = str(datetime.timedelta(seconds = duration))
    await ctx.send(f"Session ended after {human_readable_duration}.")

bot.run(BOT_TOKEN)
