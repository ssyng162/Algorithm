### 백준 10808: 알파벳 개수

num = [0]*26
S = input()

for c in S:
    num[ord(c)-97]+=1

print(*num)