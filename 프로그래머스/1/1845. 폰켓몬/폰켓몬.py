def solution(nums):
    n = len(nums)//2
    s = set(nums)

    return (n if n < len(s) else len(s))