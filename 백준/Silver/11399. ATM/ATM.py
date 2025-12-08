import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))

time.sort()

ps = [0] * (n+1)
ps[0] = 0
for i in range(1, n+1):
    ps[i] = ps[i-1] + time[i-1]

print(sum(ps))