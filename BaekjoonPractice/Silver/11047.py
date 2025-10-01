finalCount = 0
N, K = input().split(" ")
N = int(N)
K = int(K)
numbers = []
for x in range(N):
    next = int(input())
    numbers.append(next)
i = len(numbers) - 1


while K > 0 and i >= 0:
    current = numbers[i]
    if current <= K:
        count = K // current
        finalCount += count
        K -= current * count
    i -= 1
print(finalCount)
