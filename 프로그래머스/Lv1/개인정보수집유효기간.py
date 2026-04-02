# 프로그래머스: 개인정보 수집 유효기간

def to_days(date):
    y, m, d = map(int, date.split('.'))
    return y * 12 * 28 + m * 28 + d

def solution(today, terms, privacies):
    today = to_days(today)
    
    TNC = {}
    
    for term in terms:
        t, m = term.split()
        TNC[t] = int(m) * 28
    
    answer = []
    
    for idx, privacy in enumerate(privacies, start=1):
        date, term = privacy.split()
        total = to_days(date)
        total += TNC[term] - 1
        if total < today:
            answer.append(idx)
            
    return answer
