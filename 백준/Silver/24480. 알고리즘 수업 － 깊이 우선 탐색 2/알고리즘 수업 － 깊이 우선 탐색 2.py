import sys
input = sys.stdin.readline
output = sys.stdout.write

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
# 무방향 그래프
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 리스트 정렬
for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)
stack = [start]
cnt = 1
while stack:
    node = stack.pop()
    if visited[node] == 0:
        visited[node] = cnt
        cnt += 1

        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                stack.append(neighbor)

output('\n'.join(map(str, visited[1:])))