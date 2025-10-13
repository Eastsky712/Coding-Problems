N, M, V = map(int, input().split(" "))

connections = {}
for i in range(M):
    start, end = map(int, input().split(" "))
    connections.setdefault(start, [])
    connections[start].append(end)
    connections.setdefault(end, [])
    connections[end].append(start)
    connections[start].sort()
    connections[end].sort()


used = [V]

def DPS(next, used):
    current = used[-1]
    if not current in connections:
        return 
    for i in range(len(connections[current])):
        next = connections[current][i]
        if not next in used:
            used.append(next)
            DPS(next, used)


DPS(V, used)
print(*used, sep=' ')

queueW = str(V) + " "
queue = [V]
used = [V]

while queue:
    current = queue[0]
    queue.pop(0)
    if not current in connections:
        continue
    for i in range(len(connections[current])):
        next = connections[current][i]
        if not next in used:
            used.append(next)
            queue.append(next)
            queueW += str(next) + " "
    #print(queue)

print(queueW)

