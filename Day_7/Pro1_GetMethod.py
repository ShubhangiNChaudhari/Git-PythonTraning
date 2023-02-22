import requests
# Making Get Request
r = requests.get('https://archive.org/metadata/TheAdventuresOfTomSawyer_201303')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)
