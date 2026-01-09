n = int(input())
y = 2024
m = 8 + 7*(n-1)
if m > 12:
    y += m//12
    m = m % 12
    if m == 0:
        y -= 1
        m = m + 12
print(y, m)