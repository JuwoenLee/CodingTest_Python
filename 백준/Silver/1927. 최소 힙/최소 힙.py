# 최소 힙 구현 문제

import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n) :
    
    x = int(input())

    if x != 0 :
        heapq.heappush(heap, x)

    elif x == 0 :
        if len(heap) == 0 :
            print(0)
        else : 
            min = heapq.heappop(heap)
            print(min)