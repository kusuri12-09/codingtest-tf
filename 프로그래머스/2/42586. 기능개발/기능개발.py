from collections import deque 

def solution(progresses, speeds):
    answer = []
    times = [(99 - x + y) // y for x, y in zip(progresses, speeds)]
    q = deque(times)
    front = q[0]

    while q:
        cnt = 0
        front = q[0]
        while q and front >= q[0]:
            q.popleft()
            cnt += 1

        answer.append(cnt)


    return answer
