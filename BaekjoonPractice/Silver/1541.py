string = list(map(str, input().split('-')))

def add(s):
    num = list(map(int,s.split('+')))
    sum = 0
    for i in range(len(num)):
        sum += num[i]
    return sum

for i in range(len(string)):
    if '+' in string[i]:
        string[i] = add(string[i])

finalSum = int(string[0])
for i in range(1, len(string)):
    finalSum -= int(string[i])

print(finalSum)
