# 백준 21608: 상어 초등학교
import sys
input = sys.stdin.readline

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
seats = [[0] * N for _ in range(N)]
like_students = {}

for _ in range(N * N):
    score_per_seat = []
    students = list(map(int, input().split()))
    student, likes = students[0], students[1:]
    like_students[student] = likes

    for r in range(N):
        for c in range(N):
            if seats[r][c] != 0:
                continue

            liked_cnt = 0
            empty_cnt = 0

            for dx, dy in DIRS:
                nr = r + dx
                nc = c + dy
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if seats[nr][nc] == 0:
                    empty_cnt += 1
                    continue
                if seats[nr][nc] in likes:
                    liked_cnt += 1

            score_per_seat.append((liked_cnt, empty_cnt, r, c))

    score_per_seat.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    seats[score_per_seat[0][2]][score_per_seat[0][3]] = student

total = 0
score_map = [0, 1, 10, 100, 1000]

for r in range(N):
    for c in range(N):
        count = 0
        student = seats[r][c]
        for dx, dy in DIRS:
            nr = r + dx
            nc = c + dy
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if seats[nr][nc] in like_students[student]:
                count += 1
        total += score_map[count]

print(total)
