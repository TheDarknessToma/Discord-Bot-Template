import discord
import os
import asyncio
import requests
import json
from keep_alive import keep_alive
from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Your status"))
    print('Logged in!')

@client.event
async def on_message(message):

	if message.content.startswith('!hi'):
	    await message.channel.send('Hello!')

keep_alive()
client.run(os.getenv('TOKEN'))

#If you use repl.it, go to .env and paste the token.
#If your project is not public, you can edit "client.run(os.getenv('TOKEN'))" to "client.run('your token')" and delete ".env" file!
