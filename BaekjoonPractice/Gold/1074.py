N, r, c = map(int, input().split(" "))

graph = [[0 for x in range(2**(N))] for y in range(2**(N))]
complete = [[False for x in range(2**(N))] for y in range(2**(N))]

count = 1
step = 1

def Z(x, y, count, step, graph, complete):
    complete[y][x] = True
    if step == 1 or step == 3:
        if(complete[y][x+1] == False):
            graph[y][x+1] = count
            count += 1
            step += 1
            Z(x+1, y, count, step, graph, complete)
    elif step == 2:
        if(complete[y+1][x-1] == False):
            graph[y+1][x-1] = count
            count += 1
            step += 1
            Z(x-1, y+1, count, step, graph, complete)



Z(0,0, count, step, graph, complete)


def nicePrint(arr):
    for i in range(len(arr)):
        print(arr[i])
nicePrint(graph)