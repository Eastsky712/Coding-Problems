import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
num = list(map(int, input(). split(" ")))

prefix = [0] * (N+1)
for i in range(1,N+1):
    prefix[i] = prefix[i-1] + num[i-1]

out = []
for x in range(M):
    start, end = map(int, input().split(" "))
    total = prefix[end] - prefix[start-1]
    out.append(str(total))

sys.stdout.write("\n".join(out))