# 백준 11005: 진법 변환 2

import sys
input = sys.stdin.readline

def to_base(n, base):
    if n == 0:
        return "0"
        
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    
    while n > 0:
        n, remainder = divmod(n, base)
        result.append(digits[remainder])
        
    return ''.join(reversed(result))

N, B = map(int, input().split())
print(to_base(N, B))