T = int(input())


def pad(n, pS):
    if not n in pS:
        pS[n] = pad(n-1, pS) + pad(n-5, pS)
    return pS[n]



for x in range(T):
    padovanSequence = {1:1, 2:1, 3:1, 4:2, 5:2}
    n = int(input())
    #for i in range(5, n):
    #    pad(i)
    print(pad(n, padovanSequence))
    


