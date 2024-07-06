import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
integerArray = list(map(int, input().split()))
sumArray = [0]
temp = 0

for i in integerArray :
    temp += i
    sumArray.append(temp)

for _ in range(M) :
    i, j = map(int, input().split())
    print(sumArray[j] - sumArray[i - 1]) 