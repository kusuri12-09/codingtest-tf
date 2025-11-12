n,m,k = map(int,input().split())

if n // 2 >= m:
    t = m
    n -= t*2
    m -= t
    a = n + m
else:
    t = n // 2
    n -= t*2
    m -= t
    a = n + m

if a >= k:
    print(t)
else:
    while True:
        a += 3
        t -= 1
        if k <= a:
            break

    print(t)