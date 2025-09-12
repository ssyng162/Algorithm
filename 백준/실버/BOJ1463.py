### 백준 1463: 1로 만들기

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

dp[1] = 0

for i in range(2, N+1):
    dp[i] = 1 + min(
        dp[i - 1],
        (dp[i // 2] if i % 2 == 0 else float('inf')),
        (dp[i // 3] if i % 3 == 0 else float('inf'))
    )
    
print(dp[N])