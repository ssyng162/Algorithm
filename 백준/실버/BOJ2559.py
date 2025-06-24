### 백준 2559: 수열

N, K = map(int, input().split())
temp = list(map(int, input().split()))

win_sum = sum(temp[:K])
max_temp = win_sum

for i in range(K, N):
    win_sum = win_sum - temp[i-K] + temp[i]
    max_temp = max(win_sum, max_temp)

print(max_temp)