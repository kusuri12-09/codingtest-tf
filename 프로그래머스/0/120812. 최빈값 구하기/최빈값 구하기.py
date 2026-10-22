from collections import Counter

def solution(array):
    if len(array) == 1: 
  	    return array[0]
    cnt = Counter(array).most_common(2)
    return (cnt[0][0] if len(cnt) == 1 else -1 if cnt[0][1] == cnt[1][1] else cnt[0][0])