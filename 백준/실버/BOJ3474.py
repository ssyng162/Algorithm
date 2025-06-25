### 백준 3474: 교수가 된 현우

def count_0(N):    
    count = 0
    divisor = 5
    while divisor <= N:
        count += N // divisor
        divisor *= 5
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_0(N))