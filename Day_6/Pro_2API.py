import requests

url = 'https://www.reddit.com/r/Wallstreetbets/top.json?limit=10&t=year'
headers = {'User-agent': 'Mozilla/5.0'} # User agent to avoid 429 status code (Too many requests)

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
except requests.exceptions.HTTPError as e:
    print(f'Request failed: {e}')
    exit()

# Extract post data from the response
data = response.json()['data']['children']
tournament_data = []
for post in data:
    post_data = {
        'title': post['data']['title'],
        'author': post['data']['author'],
        'upvotes': post['data']['ups']
    }
    tournament_data.append(post_data)

# Define name and status
name = "r/WallStreetBets Top Posts"
status = "Active"

# Print tournament data, name, and status
print(f'Tournament data: {tournament_data}')
print(f'Name: {name}')
print(f'Status: {status}')
