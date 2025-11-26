import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())

stack = []
result = []
for i in range(n):
    line = input().split()
    command = line[0]

    if command == "1":
        x = line[1]
        stack.append(x)

    elif command == "2":
        result.append(stack.pop() if stack else "-1")
    elif command == "3":
        result.append(str(len(stack)))
    elif command == "4":
        result.append("1" if not stack else "0")
    elif command == "5":
        result.append(stack[-1] if stack else "-1")

output("\n".join(result))