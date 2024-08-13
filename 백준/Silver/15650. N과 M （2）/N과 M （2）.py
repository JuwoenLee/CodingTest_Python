import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ansList = []

def dfs() :
    if len(ansList) == M and checkOrder(ansList):
        print((' ').join(map(str, ansList)))
    
    for i in range(1, N + 1) :
        if i not in ansList :
                ansList.append(i)
                dfs()
                ansList.pop()

def checkOrder(checkList) :
    if checkList == sorted(checkList) : 
            return True
    return False

dfs()