from collections import defaultdict
N = int(input())
count = defaultdict(int)

fruits = list(map(int, input().split()))
maxLen = 0
distinct = 0
left = 0

for right in range(N):
    fruit = fruits[right]

    if count[fruit] == 0:
        distinct += 1
    count[fruit] += 1

    while distinct > 2:
        leftFruit = fruits[left]
        count[leftFruit] -= 1
        if count[leftFruit] == 0:
            distinct -= 1
        left += 1
    maxLen = max(maxLen, right - left + 1)


print(maxLen)

    
    







"""
def check(dq):
    return len(set(dq))

def takeOut(dq):
    global maxLen

    uniqueCount = check(dq)

    if uniqueCount <= 2:
        if len(dq) > maxLen:
            maxLen = len(dq)
        return
    
    if len(dq) <= maxLen:
        return
    

    dq1 = deque(islice(dq, 0, len(dq) - 1))
    dq2 = deque(islice(dq, 1, len(dq)))
    
    takeOut(dq1)
    takeOut(dq2)

takeOut(myDeque)

print(maxLen)
"""





