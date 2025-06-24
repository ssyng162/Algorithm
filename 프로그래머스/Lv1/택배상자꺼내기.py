### 프로그래머스: 택배 상자 꺼내기

def solution(n, w, num):
    target_floor=find_floor(num, w)
    top_floor=find_floor(n, w)
    target_column=find_column(num, w, target_floor)
    top_column=find_column(n, w, top_floor)
    
    print(target_floor, target_column, sep=", ")
    print(top_floor, top_column, sep=", ")
    
    result=top_floor-target_floor
    if(top_floor%2==1 and top_column<=target_column): result+=1
    if(top_floor%2==0 and top_column>=target_column): result+=1
    
    return result
    
def find_floor(num, w):
    total=0
    if(num<=w): return 0
    while(num>w):
        num-=w
        total+=1
    return total

def find_column(num, w, floor):
    if(floor%2!=0):
        return w-(num-(w*floor)-1)-1
    else:
        return num-(w*floor)-1