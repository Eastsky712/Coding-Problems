num = [0 for _ in range(30)]
for i in range(28):
    curN = int(input())
    num[curN-1] = 1

for i in range(30):
    if num[i] == 0:
        print(i+1)