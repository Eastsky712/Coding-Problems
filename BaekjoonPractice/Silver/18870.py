import sys

N = int(input())

key = [i for i in range(N)]
num = list(map(int, sys.stdin.read().split()))
values = sorted(list(set(num)))
copy = dict(zip(values, key))
result = []
for i in range(N):
    result.append(str(copy.get(num[i])))

print(" ".join(result))
