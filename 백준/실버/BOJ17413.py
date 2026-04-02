# 백준 17413: 단어 뒤집기 2

s = input()
idx = 0

answer = []
tmp = []
while idx < len(s):
    
    if s[idx] == '<':
        answer.extend(tmp[::-1])
        tmp = []
        
        while s[idx] != '>':
            answer.append(s[idx])
            idx += 1
        answer.append('>')
    elif s[idx] == " ":
        answer.extend(tmp[::-1])
        answer.append(" ")
        tmp = []
    else:
        tmp.append(s[idx])
    idx += 1
answer.extend(tmp[::-1])
print(''.join(answer))
