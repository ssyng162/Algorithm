# 프로그래머스: 완주하지 못한 선수

def solution(participant, completion):
    counts = {}
    
    for name in participant:
        counts[name] = counts.get(name, 0) + 1
    
    for name in completion:
        counts[name] -= 1
        if counts[name] == 0:
            del counts[name]
    
    return next(iter(counts))
