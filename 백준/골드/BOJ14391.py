### 백준 14391: 종이 조각

row, column = map(int, input().split())
paper = [list(map(int, input().strip())) for _ in range(row)]

answer = 0

for mask in range(1 << (row * column)):
    total = 0
    
    for r in range(row):
        cur = 0
        bits = mask >> (r * column)
        for c in range(column):
            if (bits & 1) == 0:
                cur = cur * 10 + paper[r][c]
            else:
                total += cur
                cur = 0
            bits >>= 1
        total += cur
    
    for c in range(column):
        cur = 0 
        for r in range(row):
            idx = r * column + c
            if (mask >> idx) & 1:
                cur = cur * 10 + paper[r][c]
            else:
                total += cur
                cur = 0
        total += cur
    
    answer = max(answer, total)

print(answer)