import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

close = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            card_sum = cards[i] + cards[j] + cards[k]
            if abs(m - card_sum) < abs(m-close) and card_sum <= m:
                close = card_sum
print(close)