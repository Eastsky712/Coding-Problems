N, M = map(int, input().split())

maze = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        row = list(map(int, line))
        maze.append(row)
    except EOFError:
        break

def maze_solver():
    queue = [(0,0)]
    visited = {(0,0): 1}

    directions = [[0,-1],[-1,0],[0,1],[1,0]]
    while queue:
        current = queue.pop(0)
        if current[0] == N-1 and current[1] == M-1:
                    return visited[(N-1,M-1)]
        for dir in directions:
            
            x = current[0] + dir[0]
            y = current[1] + dir[1]
            if 0 <= x <= len(maze) - 1 and 0 <= y <= len(maze[0]) - 1:
                if maze[x][y] == 1: 
                    if (x, y) not in visited:
                        visited[(x, y)] = visited[current] + 1
                        queue.append((x, y))

print(maze_solver())