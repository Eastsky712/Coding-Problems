file_name = 'coding_practice/file_exceptions/learning_python.txt'

with open(file_name) as file_object:
    content = file_object.read()

print(content.replace("Python", "C"))

with open(file_name) as file_object:
    for line in file_object:
        
        print(line.replace('Python', 'C').strip())

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace("Python", "C").strip())



