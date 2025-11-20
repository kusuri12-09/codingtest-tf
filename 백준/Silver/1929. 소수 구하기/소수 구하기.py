import sys
input = sys.stdin.readline
output = sys.stdout.write

m,n = map(int,input().split())

# 소수 구하기
prime = [True] * (n+1)
prime[0] = prime[1] = False

for i in range(2, int(n**0.5)+1):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = False
prime_numbers = [str(num) for num, p in enumerate(prime) if p and num >= m]

output("\n".join(prime_numbers))