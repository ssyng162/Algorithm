# 백준 2240: 자두나무

T, W = map(int, input().split())
plum_tree = [0] + [int(input()) for _ in range(T)]

dp = [[0] * (W+1) for _ in range(T+1)]

for t in range(1, T+1):
    dp[t][0] = dp[t-1][0] + (1 if plum_tree[t] == 1 else 0)
    for w in range(1, min(W, t) + 1):
        cur_tree = 1 if w % 2 == 0 else 2
        dp[t][w] = max(dp[t-1][w], dp[t-1][w-1]) + (1 if cur_tree == plum_tree[t] else 0)

print(max(dp[T][w] for w in range(W+1)))