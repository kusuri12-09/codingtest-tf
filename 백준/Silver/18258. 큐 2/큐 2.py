import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    command = input().strip()
    if command.startswith("push"):
        cmd, val = command.split()
        q.append(val)
    elif command == "pop":
        print(q.popleft() if q else -1)
    elif command == "size":
        print(len(q))
    elif command == "empty":
        print(1 if not q else 0)
    elif command == "front":
        print(q[0] if q else -1)
    elif command == "back":
        print(q[-1] if q else -1)