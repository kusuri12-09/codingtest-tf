import sys
input = sys.stdin.readline

number = [True] * 31
number[0] = False
for i in range(28):
    n = int(input())
    number[n] = False

for i in range(1, 31):
    if number[i]:
        print(i)