# 백준 11866: 요세푸스 문제 0

from collections import deque

N, K = map(int, input().split())

people = deque(range(1, N + 1))
result = []

while people:
    people.rotate(-(K - 1))
    result.append(str(people.popleft()))

print(f"<{', '.join(result)}>")
