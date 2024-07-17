import sys
input = sys.stdin.readline

N = int(input())
numList = []
for _ in range(N) :
    numList.append(int(input()))

numList.sort()

for n in numList :
    print(n)