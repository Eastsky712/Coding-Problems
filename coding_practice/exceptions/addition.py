print("Enter two numbers that you wish to add")
print("Enter 'q' to Quit")

while True:
    number_one = input("\nFirst Number: ")
    if number_one == 'q':
        break
    number_two = input("Second Number: ")
    if number_two == 'q':
        break
    try:
        answer = int(number_one) + int(number_two)
    except ValueError:
        print("You must input two numbers")
    else:
        print(f"{number_one} + {number_two} = {answer}")