from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

# n - 1개의 연결 정보 저장
for _ in range(n - 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 노드 1은 루트, 따라서 루트 정보 없음 = 0 저ㅇ
parent[1] = 0
queue = deque()
# 탐색 큐에 루트 노드 저장
queue.append(1)

# 큐가 빌 때 까지
while queue :
    # 기준 노드 설정
    current = queue.popleft()
    # 부모 노드 저장
    for node in graph[current] :
        # 부모 노드의 대한 정보가 업데이트되지 않았다면
        if parent[node] == 0 :
            # 현재 값을 노드의 부모 노드로 저장
            parent[node] = current
            queue.append(node)

print('\n'.join(map(str, parent[2 : ])))