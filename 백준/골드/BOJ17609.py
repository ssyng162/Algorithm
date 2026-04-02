# 백준 17609: 회문

import sys
input = sys.stdin.readline

def check(word, left, right, have_exception):
    while left <= right:
        if word[left] == word[right]: 
            left += 1
            right -= 1
        else:
            if have_exception:
                return 2
            except_left = check(word, left + 1, right, True)
            except_right = check(word, left, right - 1, True)
            if except_left == 1 or except_right == 1:
                return 1
            else:
                return 2
    return 1 if have_exception else 0

T = int(input())

for _ in range(T):
    word = input().strip()
    print(check(word, 0, len(word) - 1, False))