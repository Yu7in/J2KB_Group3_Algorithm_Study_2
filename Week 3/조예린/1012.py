# -*- coding: utf-8 -*-
"""1012

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ebr1C49oSTF_K3n_yh3wPxAw2V64sAxg
"""

# 유기농 배추
# 문제 : 배추들이 모여있는 곳의 개수를 찾아라.
# DFS, BFS 둘 다 상관없으나 깊은 재귀가 불가능한 파이썬의 특성상 BFS로 풀었습니다.

from collections import deque

Dir = [[-1,0],[1,0],[0,-1],[0,1]]
M, N, K = 0, 0, 0

def isValid(dx, dy) :
  return (0 <= dx < M) and (0 <= dy < N)

def BFS(start, visited, MAP) :
  q = deque([start])

  while q :
    # print("q:", q)
    nextNode = q.popleft()
    for d in Dir :
      dx = nextNode[0] + d[0]
      dy = nextNode[1] + d[1]
      if isValid(dx,dy) and MAP[dy][dx] == 1 and not visited[dy][dx] :
        visited[dy][dx] = True
        q.append((dx,dy)) # append를 dx dy로 해야하는데 dy dx로 하고있었다 ^^
      
T = int(input())

for _ in range(T) :
  M, N, K = map(int, input().split())
  MAP = [[0]*(M) for _ in range(N)]
  visited = [[False]*(M) for _ in range(N)]

  for _ in range(K) :
      x, y = map(int, input().split())
      MAP[y][x] = 1 

  cnt = 0  
  for y in range(N) :
    for x in range(M) :
      if MAP[y][x] == 1 and not visited[y][x] :
        cnt += 1
        visited[y][x] = True
        BFS((x, y), visited, MAP)

  print(cnt)