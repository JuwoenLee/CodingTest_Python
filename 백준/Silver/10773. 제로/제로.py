# stack을 사용하여 올바른 장부의 총합을 구하는 문제

import sys
input = sys.stdin.readline

n = int(input())
stack = list()
total = 0

for i in range(n) :
    money = int(input())
    
    # 틀린 수(0)를 입력했다면 stack에서 제거하고 총합계에서 감산
    if money == 0 :
        total -= stack.pop()

    # 올바른 수를 입력했다면 stack에 삽입하고 총합계에 가산
    else :
        stack.append(money)
        total += money

print(total)