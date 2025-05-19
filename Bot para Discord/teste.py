import discord
import asyncio

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("BOT ONLINE")
    print(client.user.name)
    print(client.user.id)
    print('------------------')

client.run('')