import discord
import os
from dotenv import load_dotenv #Prevent's sharing secrets ex. (Discord_Token)
intents = discord.Intents.default()
load_dotenv("bot.env")
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
client.run(TOKEN)