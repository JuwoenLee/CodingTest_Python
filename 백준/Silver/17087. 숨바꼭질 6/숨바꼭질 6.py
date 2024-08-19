import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
nList = list(map(int, input().split()))

dList = []
for i in range(n) :
    dList.append(abs(m - nList[i]))

print(math.gcd(*dList))