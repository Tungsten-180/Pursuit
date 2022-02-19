def load_dotenv():
  env = open('.env', 'r')
  line = env.readlines()
  lines = {x.split("=")[0].strip() : x.split("=")[1].strip(" \n") for x in line}
  return(lines)

print(load_dotenv())
