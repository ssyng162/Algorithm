# 백준 2169: 로봇 조종하기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

# prev[j]: 이전 행에서 (i-1, j)까지의 최대 가치
prev = [area[0][0]]
for i in range(1, M):
    prev.append(area[0][i] + prev[i-1])

for i in range(1, N):
    left = [-float('inf')] * M
    right = [-float('inf')] * M

    # 왼쪽 → 오른쪽
    left[0] = prev[0] + area[i][0]
    for j in range(1, M):
        left[j] = max(prev[j], left[j-1]) + area[i][j]

    # 오른쪽 → 왼쪽
    right[-1] = prev[-1] + area[i][-1]
    for j in range(M-2, -1, -1):
        right[j] = max(prev[j], right[j+1]) + area[i][j]

    # 병합
    for j in range(M):
        prev[j] = max(left[j], right[j])

print(prev[-1])