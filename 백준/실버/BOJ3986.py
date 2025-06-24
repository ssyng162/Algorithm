### 백준 3986: 좋은 단어

N = int(input())
count = 0

for _ in range(N):
    word = input()
    if(word.count("A")%2==1 or word.count("B")%2==1):
        continue
    
    point = 0
    while(point<len(word)-1):
        if(word[point]==word[point+1]):
            word = word[:point] + word[point+2:]
            point = max(point-1, 0)
        else:
            point += 1
    if(word==""):
        count+=1
        
print(count)