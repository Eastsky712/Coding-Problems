import json
filename = 'coding_practice/storing_data/numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)