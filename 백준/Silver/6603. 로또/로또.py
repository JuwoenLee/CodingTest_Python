# 1 ~ 49까지의 숫자에서 6개를 고르는 로또
# k(k > 6)개의 수를 골라 집합 s를 만들어 그 수만 가지고 6개를 선택하는 전략

import sys
input = sys.stdin.readline

def backTracking(current, depth):
    if depth == 6:
        print(*ansList)
        return
    
    for i in range(current, len(numList)):
        ansList.append(numList[i])
        backTracking(i + 1, depth + 1)
        ansList.pop()

while True:
    inputList = list(map(int, input().split()))

    if inputList[0] == 0:
        break

    numList = inputList[1 : ]
    ansList = list()
    
    backTracking(0, 0)
    print()