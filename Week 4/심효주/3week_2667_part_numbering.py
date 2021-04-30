# 좌표 문제는 dx, dy 리스트 선언하면 접근이 쉬움
import sys
input = sys.stdin.readline

def dfs(x, y, cnt):
    # 상하좌우 탐방을 위한 리스트
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    danzi[x][y] = 0
    # 상하좌우 탐방
    for i in range(4):
        # 상화좌우 움직이면서 변하는 현 좌표
        now_x, now_y = x+dx[i], y+dy[i]
        # 예외 처리
        if now_x<0 or now_y<0 or now_x>=N or now_y>=N or not danzi[now_x][now_y]:
            continue
        cnt = dfs(now_x, now_y, cnt+1)
    return cnt

N = int(input())
danzi = [list(map(int, list(input().strip()))) for _ in range(N)]
cnt = 0
ans = []

for i in range(N):
    for j in range(N):
        if danzi[i][j] == 1:
            ans.append(dfs(i, j, 1))
print(len(ans))
# !정렬을 for문 안에서도 할 수 있구나
for i in sorted(ans):
    print(i)