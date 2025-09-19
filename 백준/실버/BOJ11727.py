### 백준 11727: 2×n 타일링 2

n = int(input())

prev = 1
cur = 3

if n == 1:
    print(prev)
    exit()
elif n == 2:
    print(cur)
    exit()
    
for i in range(3, n + 1):
    prev, cur = cur, (prev * 2 + cur) % 10007
    
print(cur)