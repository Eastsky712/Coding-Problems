N = int(input())
num = list(map(int,input().split()))
findN = int(input())
total = 0
for curN in num:
    if curN == findN:
        total += 1

print(total)

