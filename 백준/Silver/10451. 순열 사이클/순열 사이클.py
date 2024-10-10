# 순열을 이용하여 방향 그래프의 순열 사이클 개수를 구하는 프로그램

from collections import deque
import sys
input = sys.stdin.readline

def bfs(gragh, start, visited) :
    queue = deque([start])
    visited[start]  = True

    while queue :
        v = queue.popleft()
        for i in gragh[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

t = int(input())

for i in range(t) :
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    arr = list(map(int, input().split()))

    for i in range(1, n + 1) :
        graph[i].append(arr[i - 1])

    visited = [False] * (n + 1)
    count = 0

    for i in range(1, n + 1) :
        if not visited[i] :
            bfs(graph, i, visited)
            count += 1

    print(count)