import sys
input = sys.stdin.readline

N = int(input())
nList = sorted(list(map(int, input().split())))
count = 0

for n in range(N) :
    key = nList[n]
    start = 0
    end = len(nList) - 1
    while(start < end) :
        if(nList[start] + nList[end] == key) :
            if(start == n) : start += 1
            elif(end == n) : end -= 1
            else :
                count += 1
                break

        elif(nList[start] + nList[end] > key) : end -= 1
        else: start += 1

print(count)