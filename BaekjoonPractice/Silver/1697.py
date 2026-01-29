from collections import deque
N, K = map(int, input().split(' '))


def find_cow():
    queue = deque([N])
    visited = {N:0}

    while queue:
        current = queue.popleft()
        if current == K:
            return visited[K]
        calculations = [current * 2, current + 1, current - 1]
        
        for result in calculations:
            if 0 <= result <= max(N, K) + 1:
                if result not in visited:
                    visited[result] = visited[current] + 1
                    queue.append(result)
    
print(find_cow())