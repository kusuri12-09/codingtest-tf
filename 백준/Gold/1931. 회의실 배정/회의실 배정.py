import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())

meeting = []
for i in range(n):
    x, y = map(int, input().split())
    meeting.append((x,y))

meeting.sort(key=lambda x:(x[1], x[0]))

last_finish_time = 0
cnt = 0
for start, finish in meeting:
    if start >= last_finish_time:
        last_finish_time = finish
        cnt += 1

print(cnt)