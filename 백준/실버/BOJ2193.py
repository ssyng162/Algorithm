### 백준 2193: 이친수

n = int(input())

prev = 1
cur = 1

for i in range(2, n):
    prev, cur = cur, prev + cur
print(cur)