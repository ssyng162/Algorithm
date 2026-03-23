# 백준 14425: 문자열 집합

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
wordset = {input().strip() for _ in range(N)}

count = 0
for _ in range(M):
    if input().strip() in wordset:
        count += 1

print(count)
