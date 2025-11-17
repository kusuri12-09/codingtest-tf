n = int(input())
students = list(map(int, input().split()))
stack = []

result = True
cnt = 1

for i in students:
    stack.append(i)
    if stack[-1] == cnt:
        stack.pop()
        cnt += 1

    while stack and stack[-1] == cnt: # 1. 스택이 비어있지 않고, 2. 맨 위 학생이 목표 순서와 같으면
        stack.pop()
        cnt += 1

if stack:
    result = False

print("Nice" if result else "Sad")