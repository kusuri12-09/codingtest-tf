def solution(nums):
    n = len(nums)//2
    s = set(nums)

    return min(n, len(s))