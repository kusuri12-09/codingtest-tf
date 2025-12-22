# 6과 9는 하나(둘다 6), 한 세트에 6이 2개
import math

n = input()
if '9' in n:
    n = n.replace('9','6')

cnt = [0] * 9
for i in range(9):
    if i == 6:
        cnt[i] = math.ceil(n.count(str(i))/2)
    else:
        cnt[i] = n.count(str(i))

print(max(cnt))