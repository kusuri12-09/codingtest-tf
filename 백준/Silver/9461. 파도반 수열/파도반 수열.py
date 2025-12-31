import sys
input = sys.stdin.readline

t = int(input())
while t > 0:
    n = int(input())
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n+1):
        if i <= 3:
            dp[i] = 1
        elif i <= 5:
            dp[i] = 2
        else:
            dp[i] = dp[i-5] + dp[i-1]

    print(dp[n])
    t -= 1