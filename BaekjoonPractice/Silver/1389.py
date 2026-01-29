# I believe there are three steps to this question
# Step one is get the total sum of steps it takes from one x to y
# Step two is to repeat the previous step for x to all other options.
# Step three is to repeat that step for all other options.
# Now if I do this how I explained it, there will be a lot of looping, meaning 
# increasing the Big-O(N) time complexity. I want to avoid that and so the 
# first thing that came up in my mind is a recusion function in order to only repeat
# what is necessary. I want to combine that with memorization so that pathways that have
# already been crossed don't need to be crossed again. I think this is the best way
# that I can come up with. The problem now comes with how I can go through with
# This task. 
N, M = map(int, input().split())
friendship = {}

for _ in range(M):
    A, B = map(int, input().split())
    friendship.setdefault(A, [])
    friendship.setdefault(B, [])
    friendship[A].append(B)
    friendship[B].append(A)

def bacon(position, arr):
    queue = [position]
    visited = {position:0}
    
    while queue:
        current = queue.pop(0)

        for friend in arr[current]:
            if friend not in visited:
                visited[friend] = visited[current] + 1
                queue.append(friend)
    return sum(visited.values())

def start():
    relations = friendship
    li = []
    for i in range(1, N + 1):
        li.append(bacon(i, relations))
    print(li.index(min(li)) + 1)

start()