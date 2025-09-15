### 백준 1932: 정수 삼각형

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
tri = [list(map(int, input().split())) for _ in range(n)]

dp[0] = tri[0][0]

for i in range(1, n):
    dp[i] = dp[i-1] + tri[i][i]
    
    for j in range(i-1, 0, -1):
        dp[j] = max(dp[j - 1], dp[j]) + tri[i][j]
        
    dp[0] = dp[0] + tri[i][0]
        
print(max(dp))