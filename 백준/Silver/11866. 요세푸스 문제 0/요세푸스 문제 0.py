from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n+1))
result = []

for i in range(n):
    for j in range(1, k+1):
        a = q.popleft()
        if j != k:
            q.append(a)
        else:
            result.append(a)

print(f'<{(", ".join(map(str, result)))}>')