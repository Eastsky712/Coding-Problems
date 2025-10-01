N, M = input().split(" ")
N = int(N)
M = int(M)
hashes = {}

for i in range(N):
    key, val = input().split(" ")
    hashes[key] = val

for i in range(M):
    key = input()
    print(hashes[key])