valorant_teams = ["drx", "t1", "nrg", "th", "drg", "fnc"]
for team in valorant_teams:
    if team == "drx":
        print("DRX WIN")
    else:
        print("boooooo, maybe t1 is ok")
    
requested_toppings = ["sausage","pepperoni","mushroom","cheese"]
print("mushroom" in requested_toppings)


banned_users = ["Bob1884","MessiIsTheGoat77","FindersKeep3rs"]
user = "alice332"

if user not in banned_users:
    print(f"{user.title()}, you may post a response as you wish.")

alien_colors = ["red","green","blue","yellow"]
alien_color = alien_colors[1]
if alien_color[1] == "green":
    print(f"You shot down a {alien_color[1]} Alien! You get 5 points")
elif alien_color == "yellow":
    print("You got 10 points!")
elif alien_color == "red":
    print("You got 15 points!")

age = 15
if age < 2:
    print("Baby")
elif age < 4:
    print("Toddler")
elif age < 13:
    print("Kid")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Elder")

usernames = ["savoring salad","flower power","ninja extinction", "sky","fireXXwater","darkness","admin"]
if usernames:   
    for username in usernames:
        if username == "admin":
            print(f"Hello {username.title()}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")



current_users = ["steve","bob","Ben","jacob","alice","joyce"]
new_users = ["Alice","jessica","sally","chloe","christina","bob"]
for user in new_users:
    if user.lower() not in current_users:
        print(f"{user} is available to be used")
        current_users.append(user)
    else:
        print(f"{user} has already been used, please pick a new username")

output = ""
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        output += f"{number}st "
    elif number == 2:
        output += f"{number}nd "
    elif number == 3:
        output += f"{number}rd "
    else:
        output += f"{number}th "
print(output)