import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = 1
M = 1

for i in range(m) :
    N *= n
    n -= 1

for j in range(m) :
    if(m == 0) : break
    M *= m
    m -= 1

print(N // M)