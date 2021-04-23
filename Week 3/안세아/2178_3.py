from collections import deque
import sys

input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0<= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] ==1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))


N, M = map(int, input().split())

graph = []
visited = [[0] * M for _ in range(N)]
for _ in range(N):
    lists = list(map(int,input().strip("\n")))
    graph.append(lists)

print(bfs())