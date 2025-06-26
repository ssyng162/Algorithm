### 백준 1068: 트리

N = int(input())
parents = list(map(int, input().split()))
target_node = int(input())

tree = [[] for _ in range(N)]
root = -1

for child, parent in enumerate(parents):
    if parent == -1:
        root = child
    else:
        tree[parent].append(child)

def dfs(node):
    global count
    if node == target_node:
        return 0
    if not tree[node] or tree[node] == [target_node]:
        return 1
    
    total = 0
    for child in tree[node]:
        total += dfs(child)
    return total

if root != target_node:
    print(dfs(root))
else:
    print(0)