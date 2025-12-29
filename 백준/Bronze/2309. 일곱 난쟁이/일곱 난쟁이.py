import sys
input = sys.stdin.readline

dwarf = [int(input()) for _ in range(9)]
dwarf.sort()
total = sum(dwarf)
stop = False
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if dwarf[i] + dwarf[j] == total - 100:
            dwarf.pop(j)
            dwarf.pop(i)
            stop = True
            break
    if stop:
        break

for i in range(7):
    print(dwarf[i])