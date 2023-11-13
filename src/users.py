import requests


def fetchUsers(endpoint):
    response = requests.get(f"{endpoint}")
    return response.json() # list of users
    