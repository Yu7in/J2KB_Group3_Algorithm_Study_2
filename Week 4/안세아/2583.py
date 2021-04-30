from collections import deque
import sys

input = sys.stdin.readline

M, N, K = map(int, input().split())
Graph = [[0] * N for _ in range(M)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

lists = []

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            Graph[k][j] = 1


def bfs(x, y):
    q = deque()
    q.append((x, y))
    Graph[x][y] = 1
    area = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if Graph[nx][ny] == 0:
                    Graph[nx][ny] = 1
                    area += 1
                    q.append((nx, ny))
    lists.append(area)


for i in range(M):
    for j in range(N):
        if Graph[i][j] == 0:
            bfs(i, j)
lists.sort()
print(len(lists))
print(*lists)
