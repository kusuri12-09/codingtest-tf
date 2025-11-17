stack = []

n = int(input())

for i in range(n):
    command = input()

    if command.startswith("push"):
        words = command.split()
        stack.append(int(words[1]))
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])