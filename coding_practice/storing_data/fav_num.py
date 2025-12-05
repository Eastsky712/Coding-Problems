import json



def get_number():
    filename = 'coding_practice/storing_data/store_number.json'

    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def store_number():
    number = input("What is your favorite number? ")
    filename = 'coding_practice/storing_data/store_number.json'

    with open(filename, 'w') as f:
        json.dump(number, f)
    return number

def favorite_number():
    number = get_number()
    if number:
        print(f"I know your favorite number! It's {number}.")
    else:
        number = store_number()
        print(f"I'll remember your number!")

favorite_number()