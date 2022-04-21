# https://dummyapi.io/data/v1/
import requests
import json

from example.models import User

response_API = requests.get('https://dummyapi.io/data/v1/user', headers={'app-id': '626141ad4ab685609a0ecbd6'})

data = response_API.text
parse_json = json.loads(data)

user = User()

for i in parse_json["data"]:
    user.id = i["id"]
    user.title = i["title"]
    user.firstName = i["firstName"]
    user.lastName = i["lastName"]
    user.picture = i["picture"]

    user.save()
