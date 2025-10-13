import math
N = int(input())

graph = [[] * N] * N
check = [[0] * N] * N
sizes = int(math.log2(N) + 1)

for i in range(N):
    graph[i] = list(map(int,input().split(" ")))

def check(startX, startY, size, graph):
    white = True
    blue = True
    for x in range(size):
        for y in range(size):
            if graph[startX + x][startY + y] == 0:
                blue = False
            else:
                white = False
            if blue == False and white == False:
                break
        else:
            continue
        break
    if white == True:
        return 0
    elif blue == True:
        return 1
    else:
        return 2

for i in range(sizes):
    for j in range((i)*4):
        print(j)
        

            


print(graph)