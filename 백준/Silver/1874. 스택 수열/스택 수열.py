import sys
input = sys.stdin.readline

N = int(input())

inputArr = []
tmpArr = []
stackArr = []
j = 1

for i in range(N) :
    inputArr.append(int(input()))

for i in inputArr :
    
    if(len(stackArr) == 0 or stackArr[-1] < i) :
        while(j <= i) :
            stackArr.append(j)
            tmpArr.append('+')
            j += 1

    if(len(stackArr) != 0) :
        if (stackArr[-1] == i) :
            stackArr.pop()
            tmpArr.append('-')
        elif (stackArr[-1] > i) :
            print('NO')
            exit(0)

for c in tmpArr :
    print(c)