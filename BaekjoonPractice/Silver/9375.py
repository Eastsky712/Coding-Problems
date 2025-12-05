from itertools import combinations
instances = int(input())

for i in range(instances):
    itemsA = int(input())
    itemStorage = {}
    for x in range(itemsA):
        val, key = map(str, input().split(" "))
        itemStorage.setdefault(key, [])
        
        itemStorage[key].append(val)
    """
    total = 0
    for x in range(1,len(itemStorage)+1):
        arr = list(combinations(itemStorage, x))
        print(arr)
        for y in arr:
            mul = 1
            for z in range(len(y)):
                #print(itemStorage[y[z]])
                mul *= len(itemStorage[y[z]])
            total += mul
    """
    mul = 1
    for x in itemStorage:
        mul *= (len(itemStorage[x]) + 1)
    print(mul - 1)

        
    #print(itemStorage)
    #print(total)
    
