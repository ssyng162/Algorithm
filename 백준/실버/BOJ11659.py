### 백준 11659: 구간 합 구하기 4

import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
dp = [0] * (N + 1)

for i, num in enumerate(map(int, input().split()), 1):
    dp[i] = dp[i-1] + num

for _ in range(M):
    num1, num2 = map(int, input().split())
    print(dp[num2] - dp[num1 - 1])