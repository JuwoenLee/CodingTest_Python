# 우선순위 큐

from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
pq = PriorityQueue(maxsize=n)
ans = list()

for i in range(n) :
    x = int(input())

    # 입력이 0이 안니라면 (추가)
    if x != 0 :
        # 절댓값으로 우선순위와 원래 값 저장
        pq.put((abs(x), x))
    # 입력이 0이라면
    else : 
        # pq가 비어있다면 (0 출력)
        if pq.empty() :
            ans.append(0)
        # pq가 비어있지 않다면 (절댓값이 가장 작은 값)
        else : 
            ans.append(pq.get()[1])

# 답 출력
for a in ans :
    print(a)