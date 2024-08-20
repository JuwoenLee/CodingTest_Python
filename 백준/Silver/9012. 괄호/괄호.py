# 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 출력

import sys
input = sys.stdin.readline

n = int(input())

def isVPS(ps) :
    stack = list()
    for p in ps :
        if p == '(' :
            stack.append(p)

        elif len(stack) == 0 and p == ')' :
                return 'NO'
        
        if p == ')' and stack[-1] == '(' :
            stack.pop()

    if len(stack) == 0 : return 'YES'
    return 'NO'

for i in range(n) :
    print(isVPS(input()))