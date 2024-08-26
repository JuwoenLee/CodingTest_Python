# stack을 사용하여 후위 표기식을 계산하는 문제

import sys
input = sys.stdin.readline

n = int(input())
# 후위 표기식 개행문자 제거
expression = input().strip()
stack = list()
numList = list()

# 숫자 정보 입력
for i in range(n) :
    numList.append(int(input()))

for e in expression :
    if 'A' <= e <= 'Z' :
        # 유니코드를 사용하여 대응하는 숫자를 stack에 push
        stack.append(numList[ord(e) - ord('A')])
    else :
        right = stack.pop()
        left = stack.pop()

        if e == '+' :
            stack.append(left + right)
        elif e == '-' :
            stack.append(left - right)
        elif e == '*' :
            stack.append(left * right)
        elif e == '/' :
            stack.append(left / right)

print("{:.2f}".format(stack.pop()))