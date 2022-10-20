
import requests
from pprint import pprint
import base64
from github import Github
from pprint import pprint


User_input = input("Enter the github username:")

g = Github()
user = g.get_user(User_input)

for repo in user.get_repos():
    print(repo)

request = requests.get('https://api.github.com/users/' + User_input + '/repos')
json = request.json()
for i in range(0, len(json)):
  print("Project Number:", i+1)
  print("Project Name:", json[i]['name'])
  print("Project URL:", json[i]['svn_url'], "\n")