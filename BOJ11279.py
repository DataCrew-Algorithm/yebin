#BOJ11279
#최대 힙

import heapq
import sys

heap = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x!= 0:
        heapq.heappush(heap,-x)
    else:
        if heap == []:
            print(0)
        else:
            print(-(heapq.heappop(heap)))