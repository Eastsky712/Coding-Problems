import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
storage = {}
used = set()
connectionsTotal = 0

for i in range(M):
    key, value = map(int, input().split(" "))
    storage.setdefault(key, [])
    storage[key].append(value)
    storage.setdefault(value, [])
    storage[value].append(key)

def findConnection(start, storage):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in used:
            used.add(node)
            stack.extend(storage.get(node, []))
    
for n in range(1, N+1):
    if not n in used:
        findConnection(n, storage)
        connectionsTotal += 1

print(connectionsTotal)