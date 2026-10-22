def solution(prices):
    stack = []
    n = len(prices)
    answer = [0] * n

    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top

        stack.append(i)

    while stack:
        top = stack.pop()
        answer[top] = n - 1 - top
    
    return answer