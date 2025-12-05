N, M = map(int, input().split())
friendship = {}

for _ in range(M):
    A, B = map(int, input().split())
    friendship.setdefault(A, [])
    friendship.setdefault(B, [])
    friendship[A].append(B)
    friendship[B].append(A)


print(friendship)