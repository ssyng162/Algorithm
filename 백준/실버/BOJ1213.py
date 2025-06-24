### 백준 1213: 팰린드롬 만들기

import collections

name = input()
words = collections.Counter(name)
result=""
odd=""

for k, v in sorted(words.items()):
    if(v%2!=0):
        odd+=k
    result += k * (v // 2)

if len(odd)>1:
    print("I'm Sorry Hansoo")
else:
    print(result+odd+result[::-1])