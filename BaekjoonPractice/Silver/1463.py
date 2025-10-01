N = int(input())
mem = {1:0, 2:1, 3:1}

def fib(n):
    global mem
    if not n in mem:
        candidates = [fib(n-1)]
        if n % 2 == 0:
            candidates.append(fib(n//2))
        if n % 3 == 0:
            candidates.append(fib(n//3))
        mem[n] = min(candidates) + 1
    return mem[n]

def beginFib(n):
    for x in range(1,n):
        fib(x)
    print(fib(n))
beginFib(N)

