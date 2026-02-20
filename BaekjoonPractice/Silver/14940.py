from collections import deque

N, M = map(int, input().split(" "))

graph = []
result = [[-1 for x in range(M)] for x in range(N)]

for x in range(N):
    line = [int(x) for x in input().split(" ")]
    graph.append(line)

def bfs(graph, start):
    visited = {start: 0}
    queue = deque([start])
    
    directions = [[0,-1],[-1,0],[0,1],[1,0]]
    
    while queue:
        current = queue.popleft()
        
        for dir in directions:
            x = current[0] + dir[0]
            y = current[1] + dir[1]
            if 0 <= x <= N - 1 and 0 <= y <= M - 1:
                if (x,y) not in visited and graph[x][y] == 1:
                    visited[(x, y)] = 1
                    result[x][y] = result[current[0]][current[1]] + 1
                    queue.append((x, y))



for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            result[i][j] = 0
            bfs(graph, (i, j))
        if graph[i][j] == 0:
            result[i][j] = 0
            
for x in range(N):
    for y in range(M):
        print(result[x][y], end=' ')
    print()
