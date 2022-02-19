
lines = {}

def load_dotenv():
  global lines
  env = open('.env', 'r')
  line = env.readlines()
  lines = {x.split("=")[0].strip() : x.split("=")[1].strip(" \n") for x in line}
  env.close()
  #return(lines)

class os:
  def getenv(key):
    return(lines[key])

