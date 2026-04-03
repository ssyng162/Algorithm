# 백준 2156: 포도주 시식

n = int(input())
grape = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n + 1)
dp[1] = grape[1]

if n >= 2:
    dp[2] = grape[1] + grape[2]

for i in range(3, n + 1):
    dp[i] = max(
        dp[i - 1],
        dp[i - 2] + grape[i],
        dp[i - 3] + grape[i - 1] + grape[i]
    )

print(dp[n])