import math

def solution(numer1, denom1, numer2, denom2):
    d = denom1*denom2
    n = numer1*denom2 + numer2*denom1
    value = math.gcd(n, d)
    return [n // value, d // value]