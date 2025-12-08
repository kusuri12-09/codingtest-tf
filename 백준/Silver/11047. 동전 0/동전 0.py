import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0
coin_idx = len(coins) - 1
while True:
    if k == 0:
        break

    if k - coins[coin_idx] >= 0:
        k -= coins[coin_idx]
        cnt += 1
    else:
        coin_idx -= 1

print(cnt)