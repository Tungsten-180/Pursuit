import discord
#import os
from dotenv import load_dotenv, os
import htapCore as H
import gameSecurity as gs

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

menu = {"/viewTarget":"shows your target for today", "/enter":"joins the game\n\tHTAP should dm you", "/view":"shows everyone who's joined", "/getpoints":"/getpoints?(who you tagged)?(their key for today)\n\tget points for tagging today", "/score":"/score?(person)\n\tshows the score of (person)"}

@client.event
async def on_message(message):
  #SETUP ------------------------------------------
  if message.author == client.user:
    return


  string = message.content
  print(string)

  author = str(message.author).split('#')[0]
  print(author)

  id = message.author.id
  
  if string[0] != "/" and string[0] != "!":
    await message.delete()
    return
  #COMMMANDS---------------------------------------
  elif string == "/start":
    if message.author.id == int(os.getenv("id1")):
      if H.System.initiate_tag() == "try overflow":
        info = H.target_dict
      else:
        raw = "\n"+"\n".join([str(x) +'->'+ str(H.target_dict[x]) for x in H.target_dict])
        processed = "\n"+"\n".join([H.peoples[x] +"->"+ H.peoples[H.target_dict[x]] for x in H.target_dict])
        info = "success"
      message_channel = client.get_channel(int(os.getenv("botChan")))
      await message_channel.send(info)
      return
    elif message.author.id == int(os.getenv("id2")):
      if H.System.initiate_tag() == "try overflow":
        info = H.target_dict
      else:
        raw = "\n"+"\n".join([str(x) +'->'+ str(H.target_dict[x]) for x in H.target_dict])
        processed = "\n"+"\n".join([H.peoples[x] +"->"+ H.peoples[H.target_dict[x]] for x in H.target_dict])
        info = "success"
    else:
      info = "insufficient permision"

  elif string == "/viewTarget" or string == "/target":
    try:
      info = H.System.view(id)
    except Exception as e:
      print("exception",e)
      info = "Error, List problably isn't generated\nTarget Dictionary length: " + str(len(H.target_dict))
  
  elif string == "/viewPeople":
    info = H.System.viewPeoples()

  elif string == "/enter":
    info = H.System.enter(author,id)

  elif string.split('?')[0] == "/join":
    teamtoJoin = int(string.split(',')[1])
    info = H.System.join(author,teamtoJoin)

  elif string.split('?')[0] == "/getpoints":
    H.scoring.points(author,string.split('?')[1],string.split('?')[2])
    info = str(H.pstats[author])
    

  elif string.split('?')[0] == "/score":
    info = H.scoring.score(string.split('?')[1])
  # MESSAGE Delivery---------------------------
  elif string == "/menu":
    info = "Pursuit Commands:\n"+"\n".join([x +"\n\t"+ menu[x] for x in menu])
    #info = H.System.menu()
  elif string == "/help":
    info = "Pursuit Commands:\n"+"\n".join([x +"\n\t"+ menu[x] for x in menu])
    
  member = message.author
  try:
    await message.delete()
  except:
    pass
  await member.create_dm()
  await member.dm_channel.send(info)
  

client.run(TOKEN)

