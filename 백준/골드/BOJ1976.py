### 백준 1976: 여행 가자

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return
    if size[rx] > size[ry]:
        parent[ry] = rx
        size[rx] += size[ry]
    if size[rx] <= size[ry]:
        parent[rx] = ry
        size[ry] += size[rx]
        
N = int(input())
M = int(input())

parent = [i for i in range(N)]
size = [1 for i in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j]==0:
            continue
        union(i, j)
    
plans = list(map(int, input().split()))
root = find(plans[0]-1)
for plan in plans:
    if find(plan-1) != root:
        print("NO")
        exit()
print("YES")