# 참고사이트: https://velog.io/@uoayop/BOJ-10026-적록색약-Python
import sys
input = sys.stdin.readline

N = int(input().strip())
matrix = [list(input().strip()) for _ in range(N)]
# 방문 표시
visited = [[False]*N for _ in range(N)]

is_not_RG, is_RG = 0, 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    # 현재 색상(좌표) 방문
    visited[x][y] = True
    cur_color = matrix[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<N) and (0<=ny<N):
            # 현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 추가
            if visited[nx][ny] == False:
                if matrix[nx][ny] == cur_color:
                    dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i, j)
            is_not_RG += 1

# R->G
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'


visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i, j)
            is_RG += 1

print(is_not_RG, is_RG)