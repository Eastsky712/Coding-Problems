import heapq
import sys
input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    current = int(input())
    if current == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, current)
    
