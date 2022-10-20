
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



########## output   ###########


Enter the github username:poornachandu28
Repository(full_name="poornachandu28/chandu")
Repository(full_name="poornachandu28/git")
Repository(full_name="poornachandu28/github")
Repository(full_name="poornachandu28/gitpractice")
Repository(full_name="poornachandu28/kesava-")
Repository(full_name="poornachandu28/madhav")
Repository(full_name="poornachandu28/pull-request-demo")
Repository(full_name="poornachandu28/pythonchandu")
Project Number: 1
Project Name: chandu
Project URL: https://github.com/poornachandu28/chandu 

Project Number: 2
Project Name: git
Project URL: https://github.com/poornachandu28/git 

Project Number: 3
Project Name: github
Project URL: https://github.com/poornachandu28/github 

Project Number: 4
Project Name: gitpractice
Project URL: https://github.com/poornachandu28/gitpractice 

Project Number: 5
Project Name: kesava-
Project URL: https://github.com/poornachandu28/kesava- 

Project Number: 6
Project Name: madhav
Project URL: https://github.com/poornachandu28/madhav 

Project Number: 7
Project Name: pull-request-demo
Project URL: https://github.com/poornachandu28/pull-request-demo 

Project Number: 8
Project Name: pythonchandu
Project URL: https://github.com/poornachandu28/pythonchandu 


Process finished with exit code 0
