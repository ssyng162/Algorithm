# 백준 10814: 나이순 정렬

import sys
input = sys.stdin.readline

n = int(input())
users = []

for _ in range(n):
    age, name = input().split()
    users.append((int(age), name))

users.sort(key=lambda x: x[0])

for age, name in users:
    print(age, name)
