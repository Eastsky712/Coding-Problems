filename = 'coding_practice/file_exceptions/pi_million_digits.txt' 

with open(filename) as file_object:
    lines = file_object.readlines()


pi = ''
for line in lines:
    pi += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

