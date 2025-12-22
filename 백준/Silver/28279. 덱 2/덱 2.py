import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())

res = []
dq = deque()
for i in range(n):
    command = input()
    if command.startswith("1"):
        v = command.split()[1]
        dq.appendleft(v)
    elif command.startswith("2"):
        v = command.split()[1]
        dq.append(v)
    elif command.startswith("3"):
        res.append(dq.popleft() if dq else "-1")
    elif command.startswith("4"):
        res.append(dq.pop() if dq else "-1")
    elif command.startswith("5"):
        res.append(str(len(dq)))
    elif command.startswith("6"):
        res.append("0" if dq else "1")
    elif command.startswith("7"):
        res.append(dq[0] if dq else "-1")
    elif command.startswith("8"):
        res.append(dq[-1] if dq else "-1")
output("\n".join(res))