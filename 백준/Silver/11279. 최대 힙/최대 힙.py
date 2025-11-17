import heapq
import sys

input = sys.stdin.readline

heap = []

n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        print(-(heapq.heappop(heap)) if heap else 0)
    else:
        heapq.heappush(heap, -x)