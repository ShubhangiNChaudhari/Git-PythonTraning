import requests

url = "https://api.github.com/repositories/19438/commits"
response = requests.get(url)
commits = response.json()
try:
  for commit in commits:
    commit_data = {
        "Name": commit["commit"]["author"]["name"],
        "URL": commit["html_url"],
    }
except KeyError:
    if commit["verification"]:
        commit_data["verified"] = commit["verification"]["verified"]
        commit_data["reason"] = commit["verification"]["reason"]
    else:
        commit_data["verified"] = False
        commit_data["reason"] = "Verification not found"
finally:
    print(commit_data)
