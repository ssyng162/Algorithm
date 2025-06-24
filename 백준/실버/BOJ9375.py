### 백준 9375: 패션왕 신해빈

testcase = int(input())

for _ in range(testcase):
    n = int(input())
    clothes = {}
    
    for _ in range(n):
        cloth, category = input().split()
        if category in clothes:
            clothes[category]+=1
        else:
            clothes[category]=1
    
    case = 1
    
    for v in clothes.values():
        case*=v+1
    
    print(case-1)