import sys
input = sys.stdin.readline

n = int(input())
numList = list(range(1, n + 1))
ansList = list()

def backTracking() :
    if len(ansList) == n :
        print(*ansList)

    for num in numList :
        if num not in ansList :
            ansList.append(num)
            backTracking()
            ansList.pop()

backTracking()