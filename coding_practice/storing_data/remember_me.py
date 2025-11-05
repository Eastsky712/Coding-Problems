import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'coding_practice/storing_data/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = 'coding_practice/storing_data/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greets the user by name"""
    username = get_stored_username()
    
    if username:
        if input(f"Is your name {username} (y/n)? ").strip().lower() == 'y':
            print(f"Welcome back, {username}!")
            return

    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")
    
    
greet_user()
