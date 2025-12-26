### 백준 1912: 연속합

n = int(input())
numbers = list(map(int, input().split()))

pre = numbers[0]
answer = numbers[0]

for i in range(1, n):
    pre = max(pre + numbers[i], numbers[i])
    answer = max(answer, pre)
    
print(answer)