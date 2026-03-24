# 백준 11003: 최솟값 찾기

import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
nums = list(map(int, input().split()))
dq = deque()

for i, x in enumerate(nums):
    while dq and dq[0][0] < i - l + 1:
        dq.popleft()
    while dq and dq[-1][1] > x:
        dq.pop()
    dq.append((i, x))
    print(dq[0][1], end=' ')
