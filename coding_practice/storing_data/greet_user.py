import json

filename = 'coding_practice/storing_data/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

