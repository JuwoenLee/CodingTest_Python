# 양방향 큐에서 원하는 원소를 뽑아내기 위한 이동 연산 횟수를 출력하는 프로그램

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
popElements = list(map(int, input().split()))
numDq = deque(list(range(1, n + 1)))
count = 0

for e in popElements :
    while True :
        # 1번 연산 : 첫 번째 원소 뽑아내기
        if numDq[0] == e :
            numDq.popleft()
            break

        else :
            # 2번 연산 : 왼쪽으로 한 칸 이동
            # 찾는 원소가 전체 길이의 절반보다 작다면(효율적인 탐색을 위해) 왼쪽으로 이동
            if numDq.index(e) < len(numDq) / 2 :
                numDq.append(numDq.popleft())
                count += 1

            # 3번 연산 : 오른쪽으로 한 칸 이동
            else :
                numDq.appendleft(numDq.pop())
                count += 1

print(count)