### 백준 1159: 농구 경기

N = int(input())
names = [input() for _ in range(N)]
names.sort()

exist = False

count = 0
alpha = names[0][0]
for name in names:
    if(alpha==name[0]):
        count+=1
    else:
        if(count>=5):
            print(alpha, end="")
            exist = True
        alpha=name[0]
        count=1
        
if count>=5:
    print(alpha, end="")
    exist = True

if not exist: 
    print("PREDAJA")