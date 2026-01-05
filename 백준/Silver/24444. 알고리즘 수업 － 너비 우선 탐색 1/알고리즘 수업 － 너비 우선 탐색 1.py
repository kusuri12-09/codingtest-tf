from collections import deque
import sys
input = sys.stdin.readline
output = sys.stdout.write

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)
q = deque()
q.append(r)
cnt = 1
while q:
    v = q.popleft()

    if visited[v] == 0:
        visited[v] = cnt
        cnt += 1
        
        for x in graph[v]:
            q.append(x)

output('\n'.join(map(str, visited[1:])))