### 백준 12852: 1로 만들기 2

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
parent = [0] * (N+1)

dp[1] = 0

for i in range(2, N+1):
    best = i - 1
    best_cost = dp[best]

    if i % 2 == 0 and dp[i//2] < best_cost:
        best = i // 2
        best_cost = dp[best]

    if i % 3 == 0 and dp[i//3] < best_cost:
        best = i // 3
        best_cost = dp[best]

    dp[i] = best_cost + 1
    parent[i] = best
    
print(dp[N])

i = N
while True:
    print(i, end=" ")
    if i == 1:
        break
    i = parent[i]