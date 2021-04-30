import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
# velog: 1-N개 해야하니까 N+1개 생
graph = [list() for _ in range(N+1)]

# velog: 재귀함수로 간단하게
def dfs(v):
    print(v, end=' ')
    visited[v] = True
    # 모든 정점을 방문하는 반복문
    for node in graph[v]:
        if not(visited[node]):
            dfs(node)

# velog: bfs는 꼭 큐를 이용해야한다. 반드시 큐가 필요해서 덱을 임포
def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for node in graph[v]:
                q.append(node)

for _ in range(M):
    fir_node, sec_node = map(int, sys.stdin.readline().split())
    # velog
    graph[fir_node].append(sec_node)
    graph[sec_node].append(fir_node)

# velog: 가장 낮은 번호부터 방문하기 위한 정
for g in graph:
    g.sort()

# velog
visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)


