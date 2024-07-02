import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
integerArray = [[0 for j in range(N)] for i in range(N)]
sumArray = [[0 for j in range(N + 1)] for i in range(N + 1)]

# origin list input setting
for i in range(N) :
    integerArray[i] = list(map(int, input().split()))

# calculate sum list
for i in range(1, N + 1) :
    for j in range(1, N + 1) :
        sumArray[i][j] = sumArray[i][j - 1] + sumArray[i - 1][j] - sumArray[i - 1][j - 1] + integerArray[i - 1][j - 1]

# calculate and print
for _ in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    result = sumArray[x2][y2] - sumArray[x1 - 1][y2] - sumArray[x2][y1 - 1] + sumArray[x1 - 1][y1 - 1]
    print(result)