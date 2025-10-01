N = int(input())

def zFib(n, memoz):
    if not n in memoz:
        memoz[n] = zFib(n-1, memoz) + zFib(n-2, memoz)
    return memoz[n]

def oFib(n, memoo):
    if not n in memoo:
        memoo[n] = zFib(n-1, memoo) + zFib(n-2, memoo)
    return memoo[n]
def fib1(n):
    memoz = {0:1, 1:0, 2:1, 3:1}
    memoo = {0:0, 1:1, 2:1, 3:2}
    print(zFib(n, memoz), oFib(n, memoo))
    

for i in range(N):
    num = int(input())
    fib1(num)
   
