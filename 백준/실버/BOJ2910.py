### 백준 2910: 빈도 정렬

N, C = map(int, input().split())
message = list(map(int, input().split()))
freq = {}
order = {}

for idx, num in enumerate(message):
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
        order[num] = idx
        
sorted_list = sorted(freq.items(), key=lambda x: (-x[1], order[x[0]]))

result = []

for key, value in sorted_list:
    result.extend([key]*value)

print(*result)