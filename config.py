import discord
import os
from dotenv import load_dotenv #Prevent's sharing secrets ex. (DISCORD_TOKEN)
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
load_dotenv("bot.env")
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("Hello"):
        await message.channel.send("Hey!")
        print("Hello sent!")
    if message.content.startswith("Pass"):
        f = open("passwords.txt", "a")
        msg = message.content.replace("Pass","")
        f.write(msg + " " + str(message.id) + "\n")
        await message.channel.send("Your message ID: " + str(message.id))
    if message.content.startswith("Retrieve"):
        password = ""
        msg = message.content.replace("Retrieve","")
        print(msg)
        f = open("passwords.txt", "r")
        for line in f:
            if msg in line:
                print(line)
                password = line
        await message.channel.send(password.replace(msg, ""))
client.run(TOKEN)