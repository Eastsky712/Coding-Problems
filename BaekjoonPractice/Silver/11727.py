N = int(input().strip())
if N == 1:
    print(1)
elif N == 2:
    print(3)
else: 
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 3
    for i in range(2, N):
        dp[i] = dp[i-1] + (dp[i-2]*2)
    print(dp[N-1] % 10007)