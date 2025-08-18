### 백준 13244: Tree

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return False
    if rank[rx] > rank[ry]:
        parent[ry] = rx
    elif rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] == rank[ry]:
        parent[rx] = ry
        rank[ry] += 1
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    components = N
    parent = [i for i in range(N)]
    rank = [1 for _ in range(N)]
    is_tree = True
    
    if M != N - 1:
        is_tree = False
    
    for _ in range(M):
        a, b = map(int, input().split())
        if not is_tree:
            continue
        if not union(a-1, b-1):
            is_tree = False
        else:
            components -= 1
            
    if is_tree and components != 1:
        is_tree = False
        
    print('tree' if is_tree else 'graph')