from collections import deque

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs_result = []
visited = [False] * (n + 1)
stack = [start]
while stack:
    node = stack.pop()
    if visited[node]:
        continue
    visited[node] = True
    dfs_result.append(node)
    for nxt in reversed(graph[node]):
        if not visited[nxt]:
            stack.append(nxt)

visited = [False] * (n + 1)
q = deque([start])
bfs_result = []
visited[start] = True
while q:
    node = q.popleft()
    bfs_result.append(node)
    for x in graph[node]:
        if not visited[x]:
            visited[x] = True
            q.append(x)

print(*dfs_result)
print(*bfs_result)