N, M = map(int, input().split())
firstMx = []
secondMx = []
totalMx = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    firstMx.append(list(map(int, input().split())))

for i in range(N):
    secondMx.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        totalMx[i][j] = firstMx[i][j] + secondMx[i][j]


for i in range(N):
    print(*totalMx[i])

