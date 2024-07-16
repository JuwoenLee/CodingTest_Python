import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Q = deque(range(1, N + 1))

while(len(Q) > 1) : 
    Q.popleft()
    Q.append(Q.popleft())

print(Q.popleft())