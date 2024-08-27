# 정수를 저장하는 덱(Deque)을 구현하고,
# 입력으러 주어지는 명령을 처리하는 프로그램

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
numDeque = deque()

for _ in range(n) :
    instruction = input().strip()

    if instruction[: 10] == 'push_front' :
        num = int(instruction[11 : ])
        numDeque.appendleft(num)

    elif instruction[: 9] == 'push_back' :
        num = int(instruction[10 : ])
        numDeque.append(num)

    elif instruction == 'pop_front' :
        if len(numDeque) == 0 :
            print(-1)
        else : print(numDeque.popleft())

    elif instruction == 'pop_back' :
        if len(numDeque) == 0 :
            print(-1)
        else : print(numDeque.pop())

    elif instruction == 'size' :
        print(len(numDeque))

    elif instruction == 'empty' :
        if len(numDeque) == 0 :
            print(1)
        else : print(0)

    elif instruction == 'front' :
        if len(numDeque) == 0 :
            print(-1)
        else : print(numDeque[0])

    elif instruction == 'back' :
        if len(numDeque) == 0 :
            print(-1)
        else : print(numDeque[-1])