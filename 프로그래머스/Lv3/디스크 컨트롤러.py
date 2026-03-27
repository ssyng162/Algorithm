# 프로그래머스: 디스크 컨트롤러

import heapq


def solution(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: x[0])

    idx = 0
    cur_time = 0
    total_turnaround = 0
    waiting = []

    while idx < n or waiting:
        while idx < n and jobs[idx][0] <= cur_time:
            requested_time, time_cost = jobs[idx]
            heapq.heappush(waiting, (time_cost, requested_time, idx))
            idx += 1

        if waiting:
            time_cost, requested_time, _ = heapq.heappop(waiting)
            cur_time += time_cost
            total_turnaround += cur_time - requested_time
        else:
            cur_time = jobs[idx][0]

    return total_turnaround // n
