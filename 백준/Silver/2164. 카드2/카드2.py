# 카드 뭉치에서 제일 위의 카드를 버리고 그 다음 카드를 맨 뒤로 옮겨서
# 마지막 1장이 남을 때까지 반복, 그 카드를 출력하는 문제

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque(range(1, n + 1))

while len(queue) != 1 :
    queue.popleft()
    queue.append(queue.popleft())

print(queue.popleft())