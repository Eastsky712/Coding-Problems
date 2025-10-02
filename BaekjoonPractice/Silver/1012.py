import sys
sys.setrecursionlimit(10000)

N = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, field, visited, M, N):
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if field[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny, field, visited, M, N)


for i in range(N):
    M, N, K = map(int, input().split(" "))
    field = [[0 for x in range(M)] for y in range(N)]
    visited = [[False for x in range(M)] for y in range(N)]
    worms = 0

    for r in range(K):
        x, y = map(int, input().split(" "))
        field[y][x] = 1

    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                dfs(x, y, field, visited, M, N)
                worms += 1
    print(worms)


