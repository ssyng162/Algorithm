# 프로그래머스: 성격 유형 검사하기

def solution(survey, choices):
    score = [3, 2, 1, 0, 1, 2, 3]
    total_score = {}
    
    for i, s in enumerate(survey):
        left, right = s[0], s[1]
        choice = choices[i] - 1
        
        if choice < 3:
            total_score[left] = total_score.get(left, 0) + score[choice]
        elif choice == 3:
            continue
        else:
            total_score[right] = total_score.get(right, 0) + score[choice]
    
    answer = []
    
    for left, right in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        lscore = total_score.get(left, 0)
        rscore = total_score.get(right, 0)
        if lscore < rscore:
            answer.append(right)
        else:
            answer.append(left)
    
    return ''.join(answer)
