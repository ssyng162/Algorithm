# 백준 1655: 가운데를 말해요

import heapq, sys
input = sys.stdin.readline

desc = []
asc = []

N = int(input())
answer = []

for _ in range(N):
    num = int(input())
    if len(desc) > len(asc):
        heapq.heappush(asc, num)
    else:
        heapq.heappush(desc, -num)

    if asc and -desc[0] > asc[0]:
        left = -heapq.heappop(desc)
        right = heapq.heappop(asc)
        heapq.heappush(desc, -right)
        heapq.heappush(asc, left)

    answer.append(str(-desc[0]))

print('\n'.join(answer))