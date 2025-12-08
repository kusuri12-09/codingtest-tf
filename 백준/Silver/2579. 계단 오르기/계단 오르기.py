n = int(input())

stair = []
stair.append(0)
for i in range(n):
    stair.append(int(input()))

dp = [0] * (n+1)
dp[0] = 0

if n > 2:
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

    print(dp[n])

elif n == 2:
    print(stair[1] + stair[2])
elif n == 1:
    print(stair[1])