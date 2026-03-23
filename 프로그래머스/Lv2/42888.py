# 프로그래머스: 오픈채팅방

def solution(record):
    logs = []
    nickname_by_uid = {}

    for r in record:
        parts = r.split()
        command = parts[0]
        uid = parts[1]

        if command in ("Enter", "Change"):
            nickname_by_uid[uid] = parts[2]

        if command in ("Enter", "Leave"):
            logs.append((command, uid))

    msg = {
        "Enter": "들어왔습니다.",
        "Leave": "나갔습니다."
    }

    answer = []
    for command, uid in logs:
        answer.append(f"{nickname_by_uid[uid]}님이 {msg[command]}")

    return answer
