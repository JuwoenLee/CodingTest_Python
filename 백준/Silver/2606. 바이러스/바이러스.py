# 순열을 이용하여 방향 그래프의 순열 사이클 개수를 구하는 프로그램

from collections import deque
import sys
input = sys.stdin.readline

def bfs(gragh, start, visited) :
    global count
    # 시작 노드 큐 생성
    queue = deque([start])
    # 방문 처리
    visited[start]  = True

    # 큐가 empty일 때까지
    while queue :
        v = queue.popleft()
        for i in gragh[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                count += 1


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for i in range(m) :
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

bfs(graph, 1, visited)
print(count)