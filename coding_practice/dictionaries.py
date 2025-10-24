alien_0 = {'color':'green','points':5,'speed':"medium"}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

if alien_0['speed'] == 1:
    x_increment = 1
elif alien_0['speed'] == 2:
    x_increment = 2
else:
    x_increment = 3


alien_0['x_position'] += x_increment

print(f"New position: {alien_0['x_position']}")
del alien_0['points']

favorite_language = {
    'bob':'python',
    'ren':'c++',
    'ben':'ruby',
    'rain':'java',
}

print(favorite_language.get('points', 'No point assigned'))


friend_1 = {"name":"Tony","age":21,"city":"Chicago"}

glossary = {"variables":"Stores data in a keyword and can be retraced by using said keyword","list":"Can store multiple variables accessing them and remove them as needed"}

for key, value in friend_1.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for value in friend_1.values():
    print(f"{value}")

first_manual_set = {'one','two','three'}
print(first_manual_set)


enemy_1 = {'color':'green','points': 5,'speed':'slow'}
enemy_2 = {'color':'red','points': 15,'speed':'fast'}
enemy_3 = {'color':'yellow','points': 10,'speed':'medium'}

enemies = []
for enemy_num in range(30):
    new_enemy = {'color':'green','points': 5,'speed':'slow'}
    enemies.append(new_enemy)

for enemy in enemies[:3]:
    if enemy['color'] == 'green':
        enemy['color'] = 'yellow'
        enemy['points'] = 10
        enemy['speed'] = 'medium'

for enemy in enemies[:5]:
    print(enemy)
print("...\n")

print(f"Total number of enemies: {len(enemies)}")

favorite_pastimes = {
    "Dongmin": ["Gaming","Origami"],
    "Donghyun": ["Reading","Gaming"],
    "Dongjun": ["Sleeping","Studying"],
    "Donggeon": ["Soccer","Running"]
    }

for name, habits in favorite_pastimes.items():
    print(f"\n{name}'s favorite past times are:")
    for habit in habits:
        print(f"\t{habit.title()}")
    

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


friend_1 = {"name":"Tony","age":21,"city":"Chicago"}
friend_2 = {"name":"Dani","age":22,"city":"Chicago"}
friend_3 = {"name":"Kanade","age":14,"city":"Yokohama"}

friends = [friend_1, friend_2, friend_3]
for friend in friends:
    print(f"\nName: {friend['name']}")
    print(f"\tAge: {friend['age']}")
    print(f"\tCity: {friend['city']}")



pet_1 = {"type":"cat","owner_name":"Dongmin"}
pet_2 = {"type":"dog","owner_name":"Bob"}
pet_3 = {"type":"lizard","owner_name":"Lance"}

pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print(f"\nType: {pet['type']}")
    print(f"Owner's Name: {pet['owner_name']}")


favorite_places = {"David":["Paris","England","Netherlands"],"Ludwig":["Tokyo","LA"],"Sid":"Chicago"}

cities = {
    "Seoul":{
        "population":9_600_000,
        "size": 605,
        "country": "South Korea",
    },
    "Tokyo":{
        "population":37_000_000,
        "size": 2_194,
        "country" : "Japan",
    },
    "Chicago":{
        "population":2_700_000,
        "size": 600,
        "country": "United States",
    },
}


for name, city_info in cities.items():
    print(f"\n{name}")
    
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tSize: {city_info['size']}km")
    print(f"\tCountry: {city_info['country']}")