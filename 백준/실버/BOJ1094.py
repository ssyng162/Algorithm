### 백준 1094: 막대기

X = int(input())
cnt = 0
while X > 0:
    cnt += X & 1
    X >>= 1
print(cnt)