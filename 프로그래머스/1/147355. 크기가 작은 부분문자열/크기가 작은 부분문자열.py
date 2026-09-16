def solution(t, p):
    cnt = 0
    for x in range(len(t)-len(p)+1):
        if t[x:x+len(p)] <= p:
   	        cnt+=1
    return cnt