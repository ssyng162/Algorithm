### 프로그래머스 2023 KAKAO BLIND RECRUITMENT / 표 병합

def find(pos):
    r, c = pos
    path = []
    while parent[r][c] != (r, c):
        path.append((r, c))
        r, c = parent[r][c]
    for pr, pc in path:
        parent[pr][pc] = (r, c)
    return (r, c)

def updateCell(r, c, value):
    nr, nc = find((r, c))
    graph[nr][nc] = value

def updateCells(target_value, new_value):
    for r in range(50):
        for c in range(50):
            if parent[r][c] == (r,c) and graph[r][c] == target_value:
                graph[r][c] = new_value
    
def merge(r1, c1, r2, c2):
    root1 = find((r1, c1))
    root2 = find((r2, c2))
    
    if root1 == root2: return

    value1 = graph[root1[0]][root1[1]]
    value2 = graph[root2[0]][root2[1]]
    value = value1 if value1 != '' else value2

    parent[root2[0]][root2[1]] = root1
    graph[root1[0]][root1[1]] = value
    graph[root2[0]][root2[1]] = ''        
    
def unmerge(r, c):
    root = find((r, c))
    value = graph[root[0]][root[1]]
    
    targets = []
    for i in range(50):
        for j in range(50):
            if find((i, j)) == root:
                targets.append((i, j))

    for i, j in targets:
        parent[i][j] = (i, j)
        graph[i][j] = ''

    graph[r][c] = value
    
def printAnswer(r, c):
    root = find((r, c))
    value = graph[root[0]][root[1]]
    return value if value != '' else 'EMPTY'

def solution(commands):
    global graph, parent
    answer = []    
    graph = [['' for _ in range(50)] for _ in range(50)] 
    parent = [[(r, c) for c in range(50)] for r in range(50)]
    
    for command in commands:
        line = command.split()
        op = line[0]
        
        if op == 'UPDATE':
            if len(line) == 4:
                updateCell(int(line[1]) - 1, int(line[2]) - 1, line[3])
            else:
                updateCells(line[1], line[2])
        elif op == 'MERGE':
            merge(int(line[1]) - 1, int(line[2]) - 1, int(line[3]) - 1, int(line[4]) - 1)
        elif op == 'UNMERGE':
            unmerge(int(line[1]) - 1, int(line[2]) - 1)
        elif op == 'PRINT':
            ans = printAnswer(int(line[1]) - 1, int(line[2]) - 1)
            answer.append(ans)
    return answer