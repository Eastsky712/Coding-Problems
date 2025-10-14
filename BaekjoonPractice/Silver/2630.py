import math
N = int(input())

graph = [[] * N] * N
chk = [[2 for _ in range(N)] for _ in range(N)] 
sizes = int(math.log2(N) + 1)
totalBlue = 0
totalWhite = 0


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

def used(startX, startY, size, fill):
    #print("USED: " + str(startX) + " " + str(startY) + " " + str(size))
    for x in range(size):
        for y in range(size):
            #print("X: " + str(startX + x) + " Y: " + str(startY + y))
            curX = startX + x
            curY = startY + y
            chk[curX][curY] = fill
    
    

for i in range(sizes):
    curX = 0
    curY = 0
    for j in range(4 ** i):
        curPaperWidth = N // (2 ** i)

        #print(str(curX) + " " + str(curY) + " " + str(curPaperWidth))
        if(chk[curX][curY] == 2):
            result = check(curX, curY, curPaperWidth, graph)
            if result == 0:
                totalWhite += 1
                used(curX, curY, curPaperWidth, 0)
            elif result == 1:
                totalBlue += 1
                used(curX, curY, curPaperWidth, 1)
        if (curX + curPaperWidth) % N == 0:
            curX = 0
            curY += curPaperWidth
        else:
            curX += curPaperWidth
        

        if curY >= N:
            continue   
     
        

print(totalWhite)
print(totalBlue)
