import math
import sys
input = sys.stdin.readline

N = int(input())
m = 2

while m <= int(math.sqrt(N)) + 1:
    while N % m == 0:
        print(m)
        N //= m
    m += 1

if N > 1:
    print(N)