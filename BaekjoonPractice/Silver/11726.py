# ALL ONEs (9 -> 1)
# 1 1 1 1 1 1 1 1


# One 2 (9 -> 8)
# 2   1 1 1 1 1 1 1
# 1 2   1 1 1 1 1 1
# 1 1 2   1 1 1 1 1
# 1 1 1 2   1 1 1 1
# 1 1 1 1 2   1 1 1
# 1 1 1 1 1 2   1 1
# 1 1 1 1 1 1 2   1
# 1 1 1 1 1 1 1 2 

# Two 2s (9 -> 6 + 5 + 4 + 3 + 2 + 1 = 21)
# 2   2   1 1 1 1 1
# 2   1 2   1 1 1 1
# 2   1 1 2   1 1 1
# 2   1 1 1 2   1 1
# 2   1 1 1 1 2   1
# 2   1 1 1 1 1 2

# 1 2   2   1 1 1 1
# 1 2   1 2   1 1 1
# 1 2   1 1 2   1 1
# 1 2   1 1 1 2   1
# 1 2   1 1 1 1 2

# 1 1 2   2   1 1 1
# 1 1 2   1 2   1 1
# 1 1 2   1 1 2   1
# 1 1 2   1 1 1 2

# 1 1 1 2   2   1 1
# 1 1 1 2   1 2   1
# 1 1 1 2   1 1 2

# 1 1 1 1 2   2   1
# 1 1 1 1 2   1 2

# 1 1 1 1 1 2   2


# Three 2s ( 9 -> 4 + 3 + 2 + 1 + 3 + 2 + 1 + 2 + 1 + 1 = 20)
# 2   2   2   1 1 1
# 2   2   1 2   1 1
# 2   2   1 1 2   1
# 2   2   1 1 1 2

# 2   1 2   2   1 1
# 2   1 2   1 2   1
# 2   1 2   1 1 2

# 2   1 1 2   2   1
# 2   1 1 2   1 2

# 2   1 1 1 2   2
#------------------------------
# 1 2   2   2   1 1
# 1 2   2   1 2   1
# 1 2   2   1 1 2

# 1 2   1 2   2   1
# 1 2   1 2   1 2

# 1 2   1 1 2   2
#------------------------------
# 1 1 2   2   2   1
# 1 1 2   2   1 2

# 1 1 2   1 2   2
#------------------------------
# 1 1 1 2   2   2

# Four 2s (8 -> 1) If Even, then 1 if odd then (N / 2) + 1
# 2   2   2   2   1

# All ones : 1
# One 2 : N - 1
# Two 2s : (N - 3) + (N - 4) + (N - 5) ... N(N + 1)/2
# Three 2s : (N - 4) + (N - 5) + (N - 6) ...
# All 2s : Even - (1), Odd - (N / 2) + 1


"""
def cal(N):
    total = 0
    if(N < 2):
        return 1
    else:
        one = 1
        if(N > 3):
            oneTwo = N - 1
        else:
            oneTwo = 0
        print(str(one) + " " + str(oneTwo))
        total += one + oneTwo #Adds All ones and One 2 case
    maxTwos = N // 2
    for i in range(0, maxTwos-2):
        moreTwos = (((N - 3 - i)*(N - 2 - i))//2)
        print(moreTwos)
        total += moreTwos
    if(N % 2 == 0):
        total += 1
    else:
        total += (N // 2) + 1
    return total
print(cal(N))

mem = [0]*N

def go(n):
    if n < 2:
        mem[n] = n + 1
        return n + 1
    mem[n] = go(n-1) + go(n-2)
    return mem[n]

print(go(N-1))
"""


N = int(input().strip())
if N == 1:
    print(1)
elif N == 2:
    print(2)
else: 
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, N):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N-1] % 10007)
N = int(input().strip())
if N == 1:
    print(1)
elif N == 2:
    print(2)
else: 
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, N):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N-1] % 10007)