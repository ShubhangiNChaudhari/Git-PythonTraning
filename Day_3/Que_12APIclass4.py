import requests

class API:
    RepoURL = 'https://api.github.com/repositories/'

    def __init__(self, repository_id):
        self.repository_id = repository_id

    def UserData(self):
        url = f"{self.RepoURL}{self.repository_id}/commits"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [(commit['commit']['author']['name'], commit['html_url'],
                     commit['commit']['verification']['verified'],
                     commit['commit']['verification']['reason']) for commit in data]
        else:
           return f"NO any user Data Found"

api = API(19438) #Here ID using from  repository link.
commits = api.UserData()

if commits:
    for commit in commits:
        print(f"Name: {commit[0]}")
        print(f"URL: {commit[1]}")
        print(f"Verified: {commit[2]}")
        print(f"Reason: {commit[3]}")
        print("\n")
else:
    print("User_Data not featch.")




    