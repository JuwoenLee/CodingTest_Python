# 쇠막대기를 자른 총 개수를 구하는 문제

import sys
input = sys.stdin.readline

str = input().strip()
stack = list()
answer = 0

for i in range(len(str)) :
    if str[i] == '(' :
        stack.append(str[i])
    else : # 닫는 괄호였다면
        stack.pop()
        
        # 위의 pop이 레이저였다면
        if str[i - 1] == '(' :
            # 잘린 조각 추가
            answer += len(stack)
        else : # 쇠막대기의 끝이였다면 (레이저가 없어도 잘리니까)
            # 쇠막대기 하나가 잘림
            answer += 1

print(answer)