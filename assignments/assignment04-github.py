# ----------------------------------------------------------------------------------------------------------------------------------------
# Assignment 04
# ----------------------------------------------------------------------------------------------------------------------------------------
# - Write a program in python that will read a file from a repository, 
# - The program should then replace all the instances of the text "Andrew" with your name. 
# - The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).
# ----------------------------------------------------------------------------------------------------------------------------------------
# Author: Rodrigo De Martino Ucedo
# ----------------------------------------------------------------------------------------------------------------------------------------

import requests
import re
from github import Github
from config import config as cfg

# API key from the config file.
apikey = cfg['privatekey']

# Authenticate with GitHub using the API key.
g = Github(apikey)  

# Uncommented -> list all repositories of the authenticated user.
#for repo in g.get_user().get_repos():
#   print(repo.name)

# Get repository by my github and the repository name.
repo = g.get_repo("RodrigoDMU/aprivateone")
#print(repo.clone_url)

# Retrieve the file information for "test2.txt".
file_info = repo.get_contents("test2.txt")

# Get the direct URL to download the file content.
url_of_file = file_info.download_url
#print(url_of_file)

# Fetch the file content from the URL
response = requests.get(url_of_file)
content_of_file = response.text
#print (content_of_file)

# Replace "Andrew" with "Rodrigo".
replace_content = re.sub(r"\bAndrew\b", "Rodrigo", content_of_file, flags=re.IGNORECASE)
#print(replace_content)

# Update the file with the modified content.
git_hub_response = repo.update_file(file_info.path, "updated by python program assignment04-github.py", replace_content, file_info.sha)
print(git_hub_response)

# END