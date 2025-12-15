import sys
input = sys.stdin.readline

n = int(input())

# 재귀 횟수
# n=2 1회, 3 2회 4 3회 n=5 5회  === 피보나치 ㅇㅁㅇ

fib = [0] * (n + 1)
fib[1], fib[2] = 1, 1
for i in range(3, n+1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib[n], n-2)