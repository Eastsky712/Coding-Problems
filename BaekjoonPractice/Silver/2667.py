# Take input to get size of maze (N x N)
# Take input of maze layout
# Store given layout into 2d array
# Check each avaliable maze position and mark if it was visited or not
# If said position is 1, then using DPS find how big the space is and return its size
# Make sure to mark all visited spaces while doing so
# Skip any positions that have been visited 
# End loop once all positions have been visited


N = int(input())
drawing = []

for i in range(N):
    line = list(map(int, input().strip()))
    drawing.append(line)

def draw_grid(arr):
    for i in arr:
        line = "".join(str(i))
        print(line)

def spread(visited, position):
    queue = [position]

    directions = [[0,0],[0,-1],[-1,0],[0,1],[1,0]]
    count = 0
    while queue:
        current = queue.pop(0)

        for dir in directions:
            x = current[0] + dir[0]
            y = current[1] + dir[1]
            if 0 <= x <= N - 1 and 0 <= y <= N - 1:
                if drawing[x][y] == 1 and ((x,y) not in visited or visited[x,y] == 0):
                    count += 1
                    visited[(x, y)] = 1
                    queue.append((x, y))
    return count
        
        



#draw_grid(drawing)
visited = {}
areas = []

for i in range(N):
    for j in range(N):
        if drawing[i][j] == 1:
            size = spread(visited, (i,j))
            if size > 0:
                areas.append(size)
        else:
            if (i,j) not in visited:
                visited[(i,j)] = 1

areas.sort()
print(len(areas))
for num in areas:
    print(num)