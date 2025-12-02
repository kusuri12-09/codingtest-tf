n = int(input())
res = []
i = 2
while i*i <= n:
    if n % i == 0:
        res.append(i)
        n //= i
    else:
        i += 1
if n > 1:
    res.append(n)

print('\n'.join(map(str, res)))