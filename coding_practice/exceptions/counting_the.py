filename = 'coding_practice/exceptions/moby_dick.txt'

with open(filename, encoding='utf-8') as f:
    word = f.read()

the_amount = word.lower().count('the ')
print(f"There are {the_amount} 'the's in {filename}!")