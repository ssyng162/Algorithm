# 프로그래머스: 신고 결과 받기

def solution(id_list, report, k):
    reported = {}
    
    for r in set(report):
        reporter, subject = r.split()
        reported.setdefault(subject, []).append(reporter)
    
    mail_list = {}
    
    for subject, reporters in reported.items():
        if len(reporters) >= k:
            for reporter in reporters: 
                mail_list[reporter] = mail_list.get(reporter, 0) + 1
            
    return [mail_list.get(user_id, 0) for user_id in id_list]
