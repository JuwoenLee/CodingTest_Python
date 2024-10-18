from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

# m개의 동기 정보 저장
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, n) :
    visited = [False] * (n + 1)
    #(시작 노드, 깊이)
    queue = deque([(1, 0)])
    # 상근이 방문 처리
    visited[1] = True
    count = 0

    while queue :
        node, depth = queue.popleft()

        # 상근이의 친구, 친구의 친구일 경우에만 계속 진행
        if depth >= 2 : 
            continue

        # 동기 탐색
        for friend in graph[node] :
            # 방문하지 않은 친구 노드라면
            if not visited[friend] :
                visited[friend] = True
                # 친구 노드를 탐색 큐에 추가 및 깊이 + 1
                queue.append((friend, depth + 1))
                count += 1
    return count

print(bfs(graph, n))