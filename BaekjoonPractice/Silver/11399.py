N = int(input())
timeTaken = list(map(int,input().split(" ")))

timeTaken.sort()

total = 0
for i in range(1,N+1):
    added = timeTaken[i-1] * (N - i + 1)
    total += added

print(total)