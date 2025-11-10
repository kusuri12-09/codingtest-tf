n = int(input())

cnt = 0

if n % 5 == 0:
    print(n//5)
    exit()

if (n == 1) or (n == 2):
    print(-1)
    exit()

while True:
    n -= 3
    cnt += 1

    if n%5 == 0:
        cnt += n//5
        break

    if n == 0:
        break

    if (n == 1) or (n == 2):
        cnt = -1
        break

print(cnt)