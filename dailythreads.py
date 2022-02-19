import discord
#import os
from dotenv import load_dotenv, os

load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD = os.getenv("GUILD")

client = discord.Client()

#   Start UP
@client.event
async def on_ready():
  for guild in client.guilds:
    if guild.name == GUILD:
      break
  print(f'{client.user} is connected to the #following guild:\n'f'{guild.name}(id: {guild.id}#)\n')
  members = '\n - '.join([member.name for member in guild.members])
  print(f'Guild Members:\n - {members}')
  
# END^



@client.event
async def on_message(message):
  if message.author == client.user:
    return
  else:
    info = message.content
    author = message.author
    await message.delete()
    print(author,info)
    await message.channel.send(str(author)+":\n"+str(info))

client.run(TOKEN)
