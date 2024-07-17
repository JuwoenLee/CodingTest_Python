import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
pQ = PriorityQueue(maxsize=N)
ans = []

for i in range(N):
    x = int(input())
    if x != 0 : pQ.put((abs(x), x))
    else :
        if pQ.empty() : ans.append(0)
        else : ans.append(pQ.get()[1])

for a in ans :
    print(a)