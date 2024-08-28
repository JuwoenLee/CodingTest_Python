# 문서의 중요도 순으로 출력하여 원하는 문서의 출력 순서를 계산하는 프로그램

from collections import deque
import sys
input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase) :
    documentCount, order = map(int, input().split())
    importance = deque(map(int, input().split()))

    # 문서 출력 순서
    count = 1

    # 모든 문서가 출력될 때가지 반복
    while importance :
        # 가장 앞 문서의 중요도가 중요도의 최댓값보다 작다면
        if importance[0] < max(importance) :
            # 큐의 맨 뒤로 이동
            importance.append(importance.popleft())

        # 가장 앞 문서의 중요도가 최댓값과 같다면
        else :
            # 찾는 문서가 가장 왼쪽(0)이라면
            if order == 0 :
                # 반복문 탈출
                break

            # 문서를 출력 (큐에서 삭제)
            importance.popleft()
            count += 1

        # 문서 출력 후 큐의 위치 업데이트
        order = order - 1 if order > 0 else len(importance) - 1
    
    print(count)