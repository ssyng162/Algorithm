### 백준 12865: 평범한 배낭

import sys
input = sys.stdin.readline

n, max_w = map(int, input().split())

items = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (max_w + 1)
    
for w, v in items:
    for cur_w in range(max_w, w - 1, -1):
        dp[cur_w] = max(dp[cur_w], dp[cur_w - w] + v)
            
print(dp[max_w])