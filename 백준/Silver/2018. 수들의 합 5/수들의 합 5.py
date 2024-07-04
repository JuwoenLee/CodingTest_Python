import sys
input = sys.stdin.readline

N = int(input())
count, start, end, sumValue = 1, 1, 1, 1

while(end != N) :
    if(sumValue == N) :
        count += 1
        end += 1
        sumValue += end
    elif(sumValue < N) :
        end += 1
        sumValue += end
    else :
        sumValue -= start
        start += 1

print(count)