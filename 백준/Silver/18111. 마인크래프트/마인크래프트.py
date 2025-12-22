import sys
input = sys.stdin.readline

n, m, block = map(int, input().split())
ground = [list(map(int, input().split())) for i in range(n)]

min_time = float('inf')
floor = 0
for i in range(257):
    removed_block = 0
    added_block = 0
    for row in ground:
        for x in row:
            if x > i:
                removed_block += (x - i)
            else:
                added_block += (i - x)

    if block + removed_block >= added_block:
        time = (removed_block * 2) + added_block
        if time <= min_time:
            min_time = time
            floor = i

print(min_time, floor)