import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def GCF() :
    nList = []
    mList = []

    for i in range(1, N + 1) :
        if N % i == 0 :
            nList.append(i)

    for j in range(1, M + 1) :
        if M % j == 0 :
            mList.append(j)

    nSet = set(nList)
    mSet = set(mList)

    duplicate = nSet.intersection(mList)
    print(max(duplicate))
    return max(duplicate)

def LCM(gcf) :
    print(int(N * M / gcf))

gcf = GCF()
LCM(gcf)