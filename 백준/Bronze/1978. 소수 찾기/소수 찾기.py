import sys
input = sys.stdin.readline

N = int(input()) 
numList = list(map(int, input().split()))
count = 0

for n in numList :
    remainderCount = 0
    for i in range(1, n + 1) :
        if n % i == 0 :
            remainderCount += 1
    if remainderCount == 2 :
        count += 1

print(count)