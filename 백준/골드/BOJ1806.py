# 백준 1806: 부분합

import sys
input = sys.stdin.readline

N, S = map(int, input().split())

nums = list(map(int, input().split()))

start = 0
end = 0
total = 0
min_len = N + 1

while start <= end:
    if total < S:
        if end == len(nums):
            break
        total += nums[end]
        end += 1
    if total >= S:
        min_len = min(min_len, end - start)
        total -= nums[start]
        start += 1

print(min_len if min_len != N + 1 else 0)
