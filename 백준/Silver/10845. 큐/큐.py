# 큐의 명령어를 처리하는 문제

import sys
input = sys.stdin.readline

n = int(input())
queue = list()

for _ in range(n) :
    statement = input().strip()

    if statement[ : 4] == 'push' :
        num = int(statement[5 : ])
        queue.append(num)
    
    elif statement == 'pop' :
        if len(queue) == 0 :
            print(-1)
        else : 
            print(queue[0])
            queue = queue[1:]
    
    elif statement == 'size' :
        print(len(queue))

    elif statement == 'empty' :
        if len(queue) == 0 :
            print(1)
        else : print(0)

    elif statement == 'front' :
        if len(queue) == 0 :
            print(-1)
        else : print(queue[0])

    elif statement == 'back' :
        if len(queue) == 0 :
            print(-1)
        else : print(queue[-1])