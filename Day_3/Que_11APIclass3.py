import requests

class API:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None


class GithubAPI(API):
    def __init__(self):
        super().__init__("https://api.github.com")

    def get_events(self):
        endpoint = "events"
        return self.get(endpoint)


# Example usage:
api = GithubAPI()
data = api.get_events()
if data:
    print(data)
else:
    print("Error: Failed to get events data")
