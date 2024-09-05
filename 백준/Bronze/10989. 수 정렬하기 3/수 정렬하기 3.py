# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램

import sys
input = sys.stdin.readline

n = int(input())
countList = [0] * 10001

for i in range(n) :
    num = int(input())
    countList[num] += 1

for i in range(1, len(countList)) :
    if(countList[i] != 0) :
        for _ in range(countList[i]) :
            print(i)