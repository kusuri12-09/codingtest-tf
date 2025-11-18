import math
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    p = list(map(int, input().split()))
    x1, y1, r1  = p[0], p[1], p[2]
    x2, y2, r2 = p[3], p[4], p[5]

    # 두 원의 중심 사이의 거리
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # 반지름의 길이가 같으면서 두 원 사이의 거리가 0 -> 일치한다
    if r1 == r2 and distance == 0:
        print(-1)
    # 두 원 사이의 거리와 반지름의 합이 동일함 -> 접한다
    # + 내접 할 때 (한 원이 다른 원 사이의 내부에 위치할 때)
    elif distance == r1+r2 or distance == abs(r1-r2):
        print(1)
    # 삼각형 성질 이용
    # abs(r1-r2) < distance(빗변) -> 삼각형이 맞는지 확인
    # r1 + r2 > distance -> 삼각형이 맞는지 확인
    elif abs(r1-r2) < distance < r1+r2:
        print(2)
    else:
        print(0)

# 무한대 -> 좌표, 반지름 동일 == 일치한다
# 0 -> 좌표가 같으면서 반지름 다름, 원이 만나지 않음 == 만나지 않는다 (d < r)
# 1 -> 원이 접함 == 접한다 == (d == r)
# 2 -> 원이 두 점에서 만남 == 두 점에서 만난다 == (d > r)