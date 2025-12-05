num = list(map(str, input()))
total = 0
missing = 0

for i in range(len(num)):
    if num[i] != "*":
        if i % 2 == 0:
            total += int(num[i])
        else:
            total += (int(num[i]) * 3)
    else:
        missing = i

if(missing % 2 == 0):
    print(10 - ((total)%10))
else:
    for i in range(0,9):
        if((total + 3 * i) % 10) == 0:
            print(i)
            break