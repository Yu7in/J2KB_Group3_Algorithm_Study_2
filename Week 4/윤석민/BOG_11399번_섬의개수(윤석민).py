from collections import deque

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
visited = [[0] * 50 for _ in range(50)]
answer = []

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]
            if n > xx >= 0 and m > yy >= 0:
                if visited[xx][yy] == 0:
                    visited[xx][yy] = 1
                    if a[xx][yy] == a[x][y]:
                        q.append([xx,yy])  
while True:
    m,n = map(int, input().split())
    if m == 0 and n == 0:
        break
    else:    
        a = [list(map(int,input().split())) for _ in range(n)]
        visited = [[0] * m for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0:
                    if a[i][j] == 1:
                        bfs(i,j)
                        count += 1 
        answer.append(count)
for i in answer:
    print(i) 
            