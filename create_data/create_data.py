import requests
import os
import csv

username = os.environ.get('username')
password = os.environ.get('password')

if username is None or password is None:
    print("export username and password in bash, like following")
    print("export username=\"username\"")
    print("export password=\"password\"")
    exit(1)

response = requests.post('http://127.0.0.1:8000/api/login/', data={
    'username': os.environ.get('username'),
    'password': os.environ.get('password'),
})

data = response.json()
token = data['token']

with open(os.path.join(os.path.dirname(__file__), "games.csv"), "r") as f:
    reader = csv.reader(f, delimiter=",")
    for i, line in enumerate(reader):
        if i == 0:
            continue
        print('line[{}] = {}'.format(i, line))
        response = requests.post('http://127.0.0.1:8000/api/games/',
                                 headers={'Authorization': 'token ' + token},
                                 json={
                                     "game": {
                                         "title": line[0],
                                         "platform": line[1],
                                         "score": line[2],
                                         "genre": line[3],
                                         "editors_choice": True if line[4] == 'Y' else False
                                     }
                                 })
        print(response.json())
