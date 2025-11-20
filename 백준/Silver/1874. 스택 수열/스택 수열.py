import sys
input = sys.stdin.readline

n = int(input())
stack = []
res = []

cnt = 1
for i in range(n):
    number = int(input())

    while number >= cnt:
        stack.append(cnt)
        res.append("+")
        cnt += 1

    if stack[-1] != number:
        print("NO")
        exit(0)

    stack.pop()
    res.append("-")

print("\n".join(res))