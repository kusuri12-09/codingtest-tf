import sys
input = sys.stdin.readline

n, m = map(int, input().split())
black = 0b10101010
white = 0b01010101 # 0b: 이진수
board = []
for _ in range(n):
    mask = 0
    for c in input().strip():
        mask = (mask << 1) | (c == 'B')
    board.append(mask)

res = 64
for i in range(n-7):
    for j in range(m-7):
        cnt_b = cnt_w = 0
        for k in range(8):
            row = (board[i+k] >> (m-j-8)) & 0xff
            # m-j-8: 만약 m=13, j=3 일 때 2까지 시프트
            # 0xff: 0b11111111, 8자리로 만듦

            # 검정색 시작
            if k % 2 == 0:
                cnt_b += bin(row ^ black).count('1')  # bin(): 이진수 변환 함수
                cnt_w += bin(row ^ white).count('1')  # xor(^): 패턴과 다른지 검사

            # 흰색 시작
            else:
                cnt_b += bin(row ^ white).count('1')
                cnt_w += bin(row ^ black).count('1')

        res = min(res, cnt_b, cnt_w)
print(res)
