def solution(price):
    return int(price*(4/5) if price >= 500000 else price*(9/10) if price >= 300000 else price*(19/20) if price >= 100000 else price)