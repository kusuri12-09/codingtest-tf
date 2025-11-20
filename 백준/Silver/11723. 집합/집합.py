import sys
input = sys.stdin.readline
output = sys.stdout.write

# 비트마스킹으로 변경
# 비트마스크란? 정수의 이진수 표현을 자료구조로 쓰는 기법
# 최빈값 구하기와 에라토스테네스의 체와 비슷한 기법인 것 같다
# 집합 문제인데 셋을 못쓰는게 말이 됨?

m = int(input())
s = 0

for i in range(m):
    line = input().strip()

    parts = line.split()
    command = parts[0]

    if len(parts) > 1:
        value = int(parts[1])
        bit_value = 1 << (value - 1)

    if command == "add":
        # OR 연산(|): 해당 비트 위치를 1로 켬 (추가)
        s |= bit_value

    elif command == "remove":
        # NOT 연산(& ~): 해당 비트 위치를 0으로 끔 (제거)
        s &= ~bit_value

    elif command == "check":
        # AND 연산: 해당 비트 위치만 확인. 결과가 0이 아니면 (비트가 켜져있으면) 1
        if (s & bit_value) != 0:
            output("1\n")
        else:
            output("0\n")

    elif command == "toggle":
        # XOR 연산(^): 해당 비트 위치를 뒤집음 (있으면 제거, 없으면 추가)
        s ^= bit_value

    elif command == "all":
        s = (1 << 20) - 1

    elif command == "empty":
        s = 0

    else:
        sys.exit(0)