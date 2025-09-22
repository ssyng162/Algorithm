### 백준 2294: 동전 2

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]
values = sorted(set(values))

dp = [k + 1] * (k + 1)
dp[0] = 0

for value in values:
    for i in range(value, k + 1):
        dp[i] = min(dp[i], dp[i - value] + 1)

if dp[k] != (k + 1):
    print(dp[k])
else:
    print(-1)