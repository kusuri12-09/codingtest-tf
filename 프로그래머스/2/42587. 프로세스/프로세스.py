from collections import deque 

def solution(priorities, location):
    answer = (0,0)

    turn = 0
    q = deque(enumerate(priorities))
    print(q)

    while q:
        if q[0][1] < max(priority for idx, priority in q):
            q.append(q.popleft())
        else:
            out = q.popleft()
            turn += 1
            if out[0] == location:
                break

    return turn