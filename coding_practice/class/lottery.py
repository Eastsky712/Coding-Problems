from random import choice
numbers = (1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e')
my_ticket = []
for i in range(4):
    my_ticket.append(choice(numbers))

count = 0
while True:
    current_ticket = []
    for i in range(4):
        current_ticket.append(choice(numbers))
    count += 1
    if current_ticket == my_ticket:
        print(f"It took {count} pulls to win the lottery")
        break