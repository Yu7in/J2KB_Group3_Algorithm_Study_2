# -*- coding: utf-8 -*-
"""2212

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ryz0p7utNfgxEi_KZPnHaqgvewhu0CSP
"""

def _2212() :
  N = int(input())
  K = int(input())
  sensors = list(map(int, input().split()))
  
  # sensors 오름차순 정렬
  sensors.sort()

  # 인접거리 구하기
  dist = [0]*(N-1)
  for i in range(0, len(sensors)-1) :
    dist[i] = sensors[i+1]-sensors[i]

  # 인접거리 내림차순 정렬
  dist.sort(reverse=True)
  ans = 0
  for i in range(K-1, len(dist)) :
    ans += dist[i]
  
  return ans
  # (0,K-1]까지는 무시하고, (K-1,)까지 sum 구한다

print(_2212())