n = int(input())

for i in range(n):
    if (i == (n-1)):
        print('*' * (n*2-1))
    elif (i == 0):
        print(' ' * (n-1-i) + '*' * (i+1))
    else:
        print(' ' * (n-1-i) + '*' + ' ' * (i*2-1)  + '*')