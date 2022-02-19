print('Welcome to the Hunter Target Asigning Program (HTAP)')

from random import randint
import pickle
import hashlib
import gameSecurity as gs

save_status = 0

options= {1:"/enter,(psswd)",2:"/join,(team)",3:"/viewPeople",  4:"viewTeams"}#,5:"Gen. HT's"}

save_file = 'save.pickle'

MaxTeamSize = 2
peoples = {}
pstats ={}
teams = {}
tstats = {}

comp = {}
comp2 = {}
target_dict = {}

team = []

class save:
  def Save():
    global teams, comp, comp2, peoples, pstats, tstats
    fle = open(save_file,'wb')
    pickle.dump(target_dict,fle,-1)
    pickle.dump(tstats,fle,-1)
    pickle.dump(pstats,fle,-1)
    pickle.dump(peoples,fle,-1)
    pickle.dump(teams,fle,-1)
    pickle.dump(comp,fle,-1)
    pickle.dump(comp2,fle,-1)
    fle.close()
  def Load():
    try:
      global teams, comp, comp2,save_status,peoples, pstats, tstats
      fle = open(save_file,'rb')
      target_dict = pickle.load(fle)
      tstats = pickle.load(fle)
      pstats = pickle.load(fle)
      peoples = pickle.load(fle)
      teams = pickle.load(fle)
      comp = pickle.load(fle)
      comp2 = pickle.load(fle)
      fle.close()
      save_status = 1
    except Exception as e:
      print(e)

class System: 
  def check():
    if save_status == 0:
      save.Load()
 
  def menu():
    stringlist = [str(x)+".) "+options[x] for x in options]
    return("Menu::\n"+"\n".join(stringlist))
  
  def dm_start():
    pass

  def enter(name,id):
    System.check()
    print(name)
    yesno = [x for x in peoples]
    if yesno.count(name) == 0 :
      peoples[name] = id
      peoples[id] = name
      pstats[id] = [0,0]
      save.Save()
      return(f'Entered {name} into the pursuit')
    else:
      print()
      return(f'{name} already entered!')# under id# {id}')

  def entesr(name,kry):
    System.check()
    print(name)
    yesno = [peoples[x] for x in peoples]
    if yesno.count(name) == 0 :
      peoples[len(peoples)] = name
      kname = gs.user(name,kry)
      #pstats[name] = [hits,injuries]
      pstats[name] = [0,0]
      save.Save()
      return(f'Entered {name} into the pursuit')
    else:
      print('returning')
      return('Already Entered!')

  def join(id,team):
    System.check()
    print(teams)
    try:
      if len(teams[team]) < MaxTeamSize and teams[team][0] != id:
        teams[team].append(id)
        save.Save()
        return(f'Joined team{team}')
      else:
        return('already joined!')
    except KeyError:
      #create team
      teams[team] = []
      teams[team].append(id)
      #tstats[team] = [hits,injuries]
      tstats[team] = [0,0]
      save.Save()
      return(f'Created and Joined team{team}')

  def viewPeoples():
    listout = "People:\n"+"\n".join([peoples[x] for x in peoples if str(peoples[x]).isdigit() == False])
    return(listout)
  
  def view(entity):
    return(peoples[target_dict[entity]])

  def Pit():
    System.check()
    k = True
    while k == True:
      pitting = System.pit()
      if pitting == "loop":
        pass
      elif pitting == 'comp':
        k = False

  def get_target(id,rw=0):
    if rw == 0:
      return(people[target_dict[id]])
    elif rw == 1:
      return(target_dict[id])

  def initiate_tag():
    global peoples, target_dict
    System.check()
    i = 0
    k = True
    while k == True:
      initiation = System.Initiate_Tag()
      if initiation == "loop error":
        print("{}{}{}{}{}{}{}{}{}")
        i += 1
        if i >= 20:
          target_dict = {"i":i,"p":peoples,"l":len(peoples)}
          return("try overflow")
        pass
      elif initiation == "completed":
        save.Save()
        k = False

  def Initiate_Tag():
    global peoples, target_dict
    people_id = [x for x in peoples if str(x).isdigit() == True]
    print(people_id)
    #^doesn't change- Iterated through in for loop
    people_list = people_id.copy()
    print(people_list)
    #^once entry is used as a target is is .pop()ed
    target_dict = {}

    for x in range(len(people_id)):
      num = randint(0,len(people_list)-1)
      try:
        z = 0 #counter to prevent looping infinitley on last
        while people_id[x] == people_list[num]:
          if z >= len(people_list):
            return('loop error')
          num = randint(0,len(people_list)-1)
          z += 1
          print("!")
      except:
        pass
      try:
        z = 0
        while target_dict[people_list[num]] == people_id[x]:
          if z >= len(people_list):
            return('loop error')
          num = randint(0,len(people_list)-1)
          z += 1
          print('@')
      except:
        pass
      target_dict[people_id[x]] = people_list[num]
      people_list.pop(num)
    print(target_dict,'\n$$$$$$done$$$$$')
    return('completed')

      
  def pit():
    global peoples,comp2,comp
    teamnum = [x for x in range(len(peoples))]
    for x in range(len(teamnum)):
      num = randint(0,len(teamnum)-1)
      try:
        z = 0
        while x == teamnum[num]:
          if z >= len(teams[num]):
            return("loop")
          num = randint(0,len(teamnum)-1)
          print('%')
          z += 1
      except:
        print('same num^')
      try:
        z = 0
        while comp2[teamnum[num]] == x:
          if z >= len(teams[num]):
            return("loop")
          num = randint(0,len(teamnum)-1)
          print('*')
          z += 1
      except:
        print('loop^')
      #comp[team[x]] = tm[num]
      comp2[x] = teamnum[num]
      teamnum.pop(num)
      #tm.pop(num)
    comp = {teams[x][0]+" & "+teams[x][1] : teams[comp2[x]][0]+" & "+teams[comp2[x]][1] for x in comp2}
    return('comp')    

class scoring:

  def dailyGen(peopledict):
    gs.user.clear()
    for x in peopledict:
      if str(x).isdigit() == True:
        keygen = gs.user(x)
      elif str(x).isdigit() == False:
        pass
      else:
        return("error")
        
  def points(entitydigi,targetdigi,key):
    if gs.user.key(targetdigi,key) == True:
      pstats[targetdigi][1] += 1
      pstats[entitydigi][0] += 1
      save.Save()
    else:
      return("INVALID KEY")

  def score(name):
    print(pstats)
    return(pstats[peoples[name]][0]-pstats[peoples[name]][1])



save.Load()
print(peoples)

