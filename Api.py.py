import requests
username = input("Enter the github username:")
request = requests.get('https://github.com/poornachandu28/pythonchandu'+username+'/repos')
json = request.json()
for i in range(0,len(json)):
  print("Project Number:",i+1)
  print("Project Name:",json[i]['name'])
  print("Project URL:",json[i]['svn_url'],"\n")

import base64
from github import Github
from pprint import pprint

g = Github
user=g.ger_user(username)
for repo in user.get_repos():
    print(repo)