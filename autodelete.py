import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
import asyncio

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True 

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Bot logged in as {client.user}')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    await asyncio.sleep(3600) 
    try:
        await message.delete()  
        print(f"{discord.utils.utcnow()} - Deleted message: {message.content} (ID: {message.id}) at {message.created_at}")
    except (discord.Forbidden, discord.HTTPException) as e:
        print(f"Fehler beim Löschen der Nachricht: {e}")

    
client.run(os.getenv('DISCORD_TOKEN'))
