# 백준 (2164): 카드2

from collections import deque

N = int(input())
dq = deque(range(1, N + 1))

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])
