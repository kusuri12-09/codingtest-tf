import sys
input = sys.stdin.readline
output = sys.stdout.write

n, m = map(int, input().split())

data = [0] + list(map(int, input().split()))

# 누적합 이용해보기
ps = [0] * (n+1)
for i in range(1, n+1):
    ps[i] = ps[i - 1] + data[i]

for i in range(m):
    a, b = map(int, input().split())
    output(str(ps[b] - ps[a-1]) + '\n')