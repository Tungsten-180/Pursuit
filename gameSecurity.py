import hashlib
import pickle
from random import randint


chars = "abcdefghijklmnopqrstuvwxyz"

secure_save = ".secure.pickle"

hashes = {}
keys = {}

def save():
  global hashes, keys
  secSav = open(secure_save,'wb')
  pickle.dump(hashes,secSav,-1)
  pickle.dump(keys,secSav,-1)
  secSav.close()
def load():
  global hashes, keys
  try:
    secSav = open(secure_save,"rb")
    hashes = pickle.load(secSav)
    keys = pickle.load(secSav)
    secSav.close()
  except Exception as e:
    print(e)
    pass
load()



class user:
  global hashes, chars, keys
  def __init__(self,user):
    key = "".join([chars[randint(0,len(chars)-1)] for x in range(4)])
    print(key)
    keys[user] = key
    save()

  def key(user,key):
    if keys[user] == key:
      return(True)
    else:
      return(False)

  def start(entity,kry):
    #global hashes
    kry = bytes(kry,"utf-8")
    m = hashlib.md5(kry)
    print(str(m.digest()))
    hashes[entity] = m.digest()
    print(hashes)
    save()

  def check(entity, kry):
    #global hashes
    load()
    print(hashes,'@')
    hash = hashlib.md5(bytes(kry,"utf-8")).digest()
    if hashes[entity] == hash:
      return(True)
    else:
      return(False)
      
  def clear():
    #global keys
    keys = {}
    save()
    
load()

