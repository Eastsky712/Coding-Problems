# Get input N, M, and S sequence into variables
# Using N, find what the P(N) is
# Go through each element in S sequence and see how many match the P(N)



N = int(input())
M = int(input())
S = list(map(str, input().strip()))


count = 0
position = 0
while position < M:
    if S[position] == 'I':
        stack = [S[position]]

        P_count = 0
        while stack:
            current = stack.pop()
            if position + 2 < M and S[position + 1] == 'O' and S[position + 2] == 'I':
                stack.append(S[position + 2])
                P_count += 1
                position += 2
            else:
                if P_count >= N:
                    count += P_count - N + 1
                P_count = 0
    position += 1
print(count)
            
