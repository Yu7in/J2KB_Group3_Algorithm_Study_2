# -*- coding: utf-8 -*-
"""1260

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ebr1C49oSTF_K3n_yh3wPxAw2V64sAxg
"""

from collections import deque

N, M, start = map(int, input().split())
graph = {}
visited = [False]*(N+1)

for _ in range(M) :
  n1, n2 = map(int, input().split())
  
  if n1 in graph :
    graph[n1].append(n2)
  else :
    graph[n1] = [n2]

  if n2 in graph :
    graph[n2].append(n1)
  else :
    graph[n2] = [n1]

# 원래는 1부터 N+1까지 순서대로 돌아야하므로 이차열 배열로 해야하는데, 습관대로 딕셔너리로 풀어서 불필요요한 sort과정이 있었습니다.
for key in graph.keys() :
  graph[key].sort()

def DFS(start) :
  visited[start] = True
  print(start, end=' ')
  if start in graph :
    for nextNode in graph[start] :
      if not visited[nextNode] :
        DFS(nextNode)

def BFS(start) :
  queue = deque([start])
  visited[start]=True
  while queue :
    nextNode = queue.popleft()
    print(nextNode, end= ' ')
    if nextNode in graph :
      for node in graph[nextNode] :
        if not visited[node] : 
          queue.append(node)
          visited[node] = True


DFS(start)
visited = [False]*(N+1)
print()
BFS(start)