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


class PullRequestAPI(API):
    def __init__(self):
        super().__init__("https://24pullrequests.com")

    def get_user_data(self, username):
        endpoint = f"users/{username}.json"
        return self.get(endpoint)


# Example usage:
api = PullRequestAPI()
data = api.get_user_data("andrew")
if data:
    print(data)
else:
    print("Error: Failed to get user data")
