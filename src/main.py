import discord
import os
from api_req import res
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'ChatGPTBot active and running as {client.user}')

@client.event
async def on_message(message):
    
    #ignores messages from bot
    if message.author == client.user:
        return

    help="To use this PromptBot, simply type\n'!prompt' (followed by the request)\n\nFor example\n!prompt What is the weather like today!\n\nWhich will then return a message generated by ChatGPT\nRespone time depends on ChatGPT"

    if message.content.startswith("!help"):
        await message.channel.send(help)
        
    
    if message.content.startswith("!prompt"):
        req=message.content.split()
        #check if request includes atleast 2 words
        if (len(req)<2):
            await message.channel.send("Error: Enter valid string")
            return

        req=" ".join(req[1:])
        await message.channel.send(res(req))

client.run(os.getenv('DISCORD_TOKEN'))
