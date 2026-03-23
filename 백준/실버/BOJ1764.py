# 백준 1764: 듣보잡

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

no_heard = {input().rstrip() for _ in range(N)}
no_seen = {input().rstrip() for _ in range(M)}

answer = sorted(no_heard & no_seen)

print(len(answer))
print('\n'.join(answer))
