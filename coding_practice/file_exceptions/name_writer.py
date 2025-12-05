"""
filename = 'coding_practice/file_exceptions/guest.txt'

name = input("Please input your name: ")

with open(filename, 'a') as file_object:
    file_object.write(name)
"""

filename = 'coding_practice/file_exceptions/guest_book.txt'

while True:
    name = input("Please input your name (Enter 'q' to exit): ")
    
    if name == 'q':
        break

    with open(filename, 'a') as file_object:
        file_object.write(name + "\n")
        
    
    