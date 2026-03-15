# 백준 2750: 수 정렬하기

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()

print(*nums, sep="\n")
