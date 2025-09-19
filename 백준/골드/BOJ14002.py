### 백준 14002: 가장 긴 증가하는 부분 수열 4

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [1] * n
prev = [-1] * n

for i in range(1, n):
    for j in range(0, i):
        if A[j] < A[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j

idx = dp.index(max(dp))
answer = []
while idx != -1:
    answer.append(A[idx])
    idx = prev[idx]
answer.reverse()

print(max(dp))
print(*answer)
