### 백준 1717: 집합의 표현

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return
    if rank[rx] > rank[ry]:
        parent[ry] = rx
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    if rank[rx] == rank[ry]:
        parent[rx] = ry
        rank[ry] += 1
        
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [1 for _ in range(n+1)]

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0: 
        union(a, b)
    elif op == 1: 
        ra, rb = find(a), find(b)
        if ra == rb:
            print("YES")
        else:
            print("NO")