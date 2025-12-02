n = int(input())

prime = [True] * (n+1)
prime[0] = prime[1] = False

for i in range(2, int(n**0.5)+1):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = False
prime_numbers = [num for num in range(n+1) if prime[num] and n % num == 0]

res = []
for p in prime_numbers:
    while n % p == 0:
        res.append(p)
        n //= p
print('\n'.join(map(str, res)))