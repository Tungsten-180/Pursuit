#import discord
#import os
from dotenv import load_dotenv,os
import time
#import threading
from discord.ext import tasks, commands

t = time.time()
print(t)

load_dotenv()
TOKEN = os.getenv("SCHEDULER")
GUILD = os.getenv("GUILD")

botChan  = int(os.getenv("botChan"))

client = commands.Bot("!")
#client = discord.Client()


#   Start UP
@client.event
async def on_ready():
  global botChan
  for guild in client.guilds:
    if guild.name == GUILD:
      break
  print(f'{client.user} is connected to the #following guild:\n'f'{guild.name}(id: {guild.id}#)\n')
  members = '\n - '.join([member.name for member in guild.members])
  print(f'Guild Members:\n - {members}')
  print("-----------------\n")
# END^

@client.event
async def interal_message(mess):
  message_channel = client.get_channel(botChan)
  print(client.get_channel(botChan))
  await message_channel.send(mess)


@tasks.loop(hours=24)
async def DailyTag():
  global botChan
  timee = time.time() - t
  await interal_message("/start")
  print(timee)

@DailyTag.before_loop
async def before():
  await client.wait_until_ready()
  print('finished waiting')

DailyTag.start()
client.run(TOKEN)



