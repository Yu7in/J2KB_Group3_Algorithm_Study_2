# bfs로 풀어보기
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    que = deque()
    que.append((x, y))

    island[x][y] = 0

    while que:
        n = que.popleft()

        for i in range(8):
            nx = n[0] + directions[i][0]
            ny = n[1] + directions[i][1]

            if (0<=nx<h) and (0<=ny<w):
                if int(island[nx][ny]) == 1:
                    island[nx][ny] = 0
                    que.append((nx, ny))

while True:
    w, h = map(int, input().split())
    cnt = 0
    if w == 0 and h == 0:
        break
    # 입력에서 띄어쓰기 제거하고 행렬 만들기
    island = [' '.join(input()).split() for _ in range(h)]
    # print(island)

    for i in range(h):
        for j in range(w):
            if int(island[i][j]) == 1:
                cnt += 1
                bfs(i, j)

    print(cnt)