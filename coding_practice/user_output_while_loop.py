prompt = ("\nTell me something, I will repeat it back to you")
prompt += "\nEnter 'quit' to end the program:"

active = False #True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#name = input("Please enter your name: ")
#print(f"Hello, {name.title()}!")

prompt = "\nPlease enter a City you have been to before"
prompt += "\n(Enter 'quit' to end the program): "

while False: #True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


current_number = 10
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

pets = ['cat','cat','cat','cat','dog','hamster','lizard','turtle','rabbit']
#print(pets)
while 'cat' in pets:
    pets.remove('cat')
#print(pets)

sandwich_orders = []#'pastrami','meatball','cheese','pastrami','ham','fish','pastrami','chicken','beef']
finished_sandwiches = []

count = 0
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    if current_order == 'pastrami':
        print("deli has run out of pastrami")
        while 'pastrami' in sandwich_orders:
            sandwich_orders.remove('pastrami')
        continue
    print(f"I made your {current_order.title()} sandwich")
    finished_sandwiches.append(current_order)

for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich was made")

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    location = input("If you could visit one place in the world, where you would go? ")
    responses[name] = location
    cont = input("Would you like to let another person respond? (yes/no) ")
    if cont == 'no':
        polling_active = False

print('\n--- Poll Results ---')
for name, location in responses.items():
    print(f"{name.title()} would like to go to {location.title()}.")
