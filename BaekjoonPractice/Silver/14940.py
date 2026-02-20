N = int(input())

graph = {}
for x in range(N):
    line = list(map(int, input().split(" ")))
    graph.setdefault(x, [])
    for y in range(N):
        if line[y] == 1:
            
            graph[x].append(y)

def dfs(graph, start, end, visited=None):
    visited = set()
    stack = [start]
    
    while stack:
        current = stack.pop(0)
        
        for neighbor in graph[current]:
            if neighbor == end:
                return True
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(current)
    return False
                
            
result = [[0 for x in range(N)]for x in range(N)]
for i in range(N):
    for j in range(N):
        if dfs(graph, i, j):
            result[i][j] = 1
        else:
            result[i][j] = 0

for i in range(N):
    for j in range(N):
        print(result[i][j], end=' ')
    print()
