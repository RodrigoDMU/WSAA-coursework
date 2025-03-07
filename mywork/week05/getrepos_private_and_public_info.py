import requests
import json
from config2 import config as cfg

#filename = "repos-public.json"
#filename = "wsaa-code.json"
filename = "repos-private.json"

#url = 'https://api.github.com/users/RodrigoDMU/repos?per_page=100'
#url = 'https://api.github.com/repos/RodrigoDMU/WSAA-coursework/contents/code'
url = 'https://api.github.com/repos/RodrigoDMU/aprivateone'

apikey = cfg['htmltopdfkey']

#response = requests.get(url)  
response = requests.get(url, auth = ('token', apikey))
print (response.status_code)
repo_json = response.json()

with open(filename, 'w') as fp:
    json.dump(repo_json, fp, indent=4)