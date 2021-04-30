# 풀이 출처: https://gingerkang.tistory.com/40
from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0, 0))
    distance = [[0] * m for _ in range(n)]
    # 시작 위치 카운트
    distance[0][0] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if maze[ny][nx] == '1' and distance[ny][nx] == 0:
                distance[ny][nx] = distance[y][x] + 1
                q.append((nx, ny))

    return distance[n - 1][m - 1]


n, m = map(int, input().split())
maze = [input() for _ in range(n)]

print(bfs())