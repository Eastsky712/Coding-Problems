N = int(input())
number = [int(input()) for _ in range(N)]
dp_memo = [None] * N

#Rule 1: You may climb the stair one or two steps at a time.
#Rule 2: You may not climb if it will lead to a chain of three steps. The starting point is excluded from this rule
#Rule 3: You must step on the last step


def dp(n):
    if dp_memo[n] is not None:
        return dp_memo[n]

    if n == 0:
        result =  number[0]
    elif n == 1:
        result = max(number[1], number[0] + number[1])
    elif n == 2:
        result = max(number[0] + number[2], number[1] + number[2])
    if n >= 3:
        result = max(
            dp(n-2) + number[n],                #Step
            dp(n-3) + number[n-1] + number[n]   #Skip
        )
    dp_memo[n] = result
    return result

# 10 20 15 10 25 20

print(dp(N-1))