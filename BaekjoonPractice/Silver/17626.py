import math

N = int(input())

if int(math.isqrt(N)) ** 2 == N:
    print(1)
    exit()

for i in range(1, int(math.isqrt(N)) + 1):
    j = N - i * i
    if int(math.isqrt(j)) ** 2 == j:
        print(2)
        exit()

temp = N
while temp % 4 == 0:
    temp //= 4
if temp % 8 == 7:
    print(4)
else:
    print(3)
