import sys
N, M = map(int, input().split())

classroom = []
haveBeen = [[0 for _ in range(M)] for _ in range(N)]
total, iX, iY = 0, 0, 0
sys.setrecursionlimit(1000000)

for i in range(N):
    classroom.append(list(sys.stdin.readline().strip()))
    try:
        iX = classroom[i].index('I')
        iY = i
    except ValueError:
        continue

def spread(curX, curY):
    global total
    haveBeen[curY][curX] = 1
    if classroom[curY][curX] == 'P':
        total += 1

    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx, ny = curX + dx, curY + dy
        if 0 <= nx < M and 0 <= ny < N:
            if classroom[ny][nx] != 'X' and haveBeen[ny][nx] == 0:
                spread(nx, ny)
            
spread(iX, iY)   
if total == 0:
    print("TT")
else: 
    print(total)
