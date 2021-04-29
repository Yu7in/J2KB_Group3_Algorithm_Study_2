""" 참고 https://blog.naver.com/chad0909/222260584546 
    참고 https://blog.naver.com/hunii123/222310823558 """

from collections import deque

number = int(input())
a = [list(map(str, input())) for _ in range(number)] 
visited = [[0]*number for _ in range(number)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if number > xx >= 0 and number > yy >= 0:
                if visited[xx][yy] == 0 and a[x][y] == a[xx][yy]:
                    q.append((xx,yy))
                    visited[xx][yy] = 1
count = 0
count2 = 0
for i in range(number):
    for j in range(number):
        if visited[i][j] ==0:
            bfs(i,j)
            count += 1
print(count)
visited = [[0]*number for _ in range(number)]

for i in range(number):
    for j in range(number):
        if a[i][j] == "G":
            a[i][j] = "R"
for i in range(number):
    for j in range(number):
        if visited[i][j] == 0:
            bfs(i,j)
            count2 += 1
print(count2)



