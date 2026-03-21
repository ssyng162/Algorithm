# 백준 1644: 소수의 연속합

N = int(input())

if N < 2:
    print(0)
else:
    prime = [True] * (N + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(N ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, N + 1, i):
                prime[j] = False
    
    nums = []
    for i in range(2, N + 1):
        if prime[i]:
            nums.append(i)
    
    start = 0
    end = 0
    total = 0
    answer = 0
    
    while True:
        if total == N:
            answer += 1
            total -= nums[start]
            start += 1
        if total < N:
            if end == len(nums):
                break
            total += nums[end]
            end += 1
        if total > N:
            total -= nums[start]
            start += 1
    
    print(answer)