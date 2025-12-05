def display_message():
    print("In this chapter, we are learning about functions")
#display_message()

def favorite_book(title):
    print(f"One of my favorite books is {title.title()}.")
#favorite_book("chalet's web")

def describe_pet(pet_name='harry', pet_age=12, animal_type='hamster'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()} and is {pet_age} years old.")

#describe_pet('dog', 'bob', 14)

def make_shirt(size='L', text='I love Python'):
    print(f"\nThe size of the shirt is: {size.title()}")
    print(f"The message on the shirt is: {text}")

#make_shirt('L', 'When life gives you lemons, make lemonade')
#make_shirt(text='I am your father', size='M')

#make_shirt('L')
#make_shirt(size='M')
#make_shirt('M', 'I love Java')

def describe_city(city_name, country_name='South Korea'):
    print(f"{city_name.title()} is in {country_name.title()}.")

#describe_city('Seoul')
#describe_city('Busan')
#describe_city('Chicago', 'United States')


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

professional = get_formatted_name('dongmin', 'seo')
#print(professional)
professional2 = get_formatted_name('dongmin', 'jr', 'seo')

def build_person(first_name, last_name, age=None):
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

artist = build_person('bob', 'anderson', age=43)
#print(artist)

while False:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}!")

def city_country(city_name, country_name):
    return f"\"{city_name.title()}, {country_name.title()}\""

#print(city_country("Seoul",'South Korea'))

def make_album(artist_name, album_title, number_of_songs=None):
    music_albums = {'name': artist_name, 'title': album_title}
    if number_of_songs:
        music_albums['count'] = number_of_songs
    return music_albums

#print(make_album("Michael", "Funk"))
#print(make_album("Charlie", "Payphone", 6))
#print(make_album("Maroon", "Sugar"))


def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
        

messages = ['how is it going?', 'thank you!', 'fighting!']
sent_messages = []

#send_messages(messages,sent_messages)
#show_messages(messages)
#show_messages(sent_messages)

#send_messages(messages[:],sent_messages)
#print(messages)
#print(sent_messages)

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', 
                             location='princeton', 
                             field='physics')

#print(user_profile)

def sandwiches(*types):
    print("\nTypes of Sandwiches Wanted:")
    for type in types:
        print(f"- {type}")

#sandwiches('ham','beef','cheese')
#sandwiches('pork','meatball','lettuce','corn')

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('dongmin', 'seo', hobbit='gaming', height=169, languages=2)
#print(user_profile)

def make_car(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['name'] = model_name
    return car_info

car = make_car('subaru','outback', color='blue',tow_package=True)

print(car)


    

