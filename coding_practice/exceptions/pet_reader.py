filename1 = 'coding_practice/exceptions/cats.txt'
filename2 = 'coding_practice/exceptions/dogs.txt'


try:    
    with open(filename1, encoding='utf-8') as f:
        cats = f.readlines()
except FileNotFoundError:
    print(f"{filename1} does not exist")
    #pass
else:
    for cat in cats:
        print(cat.strip())

try:
    with open(filename2, encoding='utf-8') as f:
        dogs = f.readlines()
except FileNotFoundError:
    print(f"{filename2} does not exist")
    #pass
else:
    for dog in dogs:
        print(dog.strip())
