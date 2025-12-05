import sys
N, M = map(int, sys.stdin.readline().split(" "))
woodHeight = list(map(int, sys.stdin.readline().split(" ")))

def cutWood(height, wood):
    total = 0
    for h in wood:
        if h > height:
            total += h - height
    return total

low = 0
high = max(woodHeight)
best = 0

while low <= high:
    mid = (low + high) // 2
    current = cutWood(mid, woodHeight)
    #print("Current: " + str(current) + " mid: " + str(mid))
    
    if current >= M:
        best = mid
        low = mid + 1
    else:
        high = mid - 1
    
print(best)
    