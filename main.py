import os

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.find('https://www.tiktok.com/') != -1:
        # replace tiktok.com with vxtiktok.com
        url = message.content.replace('tiktok.com', 'vxtiktok.com')
        
        #add author information and delete original message
        authored_url = message.author.name + ' posted: ' + url
        await message.delete()
        await message.channel.send(authored_url)


token = os.environ['DISCORD_TOKEN']
client.run(token)
