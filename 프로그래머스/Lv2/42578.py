# 프로그래머스: 의상

def solution(clothes):
    closet = {}
    for _, category in clothes:
        closet[category] = closet.get(category, 0) + 1
        
    answer = 1
    for v in closet.values():
        answer *= (v + 1)
    
    return answer - 1
