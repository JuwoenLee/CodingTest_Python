# N명의 사람이 원으로 앉아 있을 때, K번째 사람을 추출하는 프로그램

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numList = deque(range(1, n + 1))
result = list()

# 수열이 비어있게 될 때 까지
while numList :

    # k번째 정수를 가장 앞에 두기 위해 뒤로 이동
    for i in range(k - 1) :
        numList.append(numList.popleft())

    # k번째 정수가 가장 앞일 때, 결과 리스트에 저장
    result.append(numList.popleft())

# 출력 형식
print('<{}>'.format(', '.join(map(str, result))))