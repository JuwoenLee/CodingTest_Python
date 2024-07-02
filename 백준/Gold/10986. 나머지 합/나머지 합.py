import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
originList = list(map(int, input().split()))
sumList = [0] * (N + 1)
remainderList = []
countList = [0] * M
result = 0

for i in range(1, N + 1) :
    sumList[i] = sumList[i - 1] + originList[i - 1]
    remainderList.append(sumList[i] % M)

    if(remainderList[i - 1] == 0) : result += 1
    countList[sumList[i] % M] += 1

for i in range(M) :
    if (countList[i] > 1) :
        result += countList[i] * (countList[i] - 1) // 2

print(result)