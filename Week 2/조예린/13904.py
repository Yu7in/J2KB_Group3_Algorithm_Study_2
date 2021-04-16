# -*- coding: utf-8 -*-
"""13904

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ryz0p7utNfgxEi_KZPnHaqgvewhu0CSP
"""

# 하루에 한 과제를 끝낼 수 있는데,
# 과제마다 마감일이 있으므로 모든 과제를 못끝낼 수도 있음.
# 가장 점수를 많이 받을 수 있도록 과제를 수행하고 싶다.

# N : 과제의 개수
# d : 과제 마감일까지 남은 일수
# w : 과제의 점수

from collections import deque
import copy

def _13904() :
  ans = 0
  N = int(input())
  works = [[0]*2 for _ in range(N)]
  for i in range(N) :
    works[i][0], works[i][1] = map(int, input().split())
  
  works.sort(key = lambda x : (-x[0], -x[1]))
  works = deque(works) # popleft를 쓰기 위함 (deque의 popleft는 O(1)이다.)
  maxDay = (works[0])[0] # 최대 마감일

  while works :
    if maxDay <= 0 : break
    todayWork = [] # maxDay에 할 수 있는 작업 배열
    tempWorks = copy.deepcopy(works)
    
    for work in tempWorks :
      if work[0] >= maxDay :
        todayWork.append(works.popleft())
      else : break

    if todayWork :
      todayWork.sort(key = lambda x : (-x[1]))
      todayWork = deque(todayWork)
      ans += (todayWork.popleft())[1]
      works = list(works) + list(todayWork)
    
    works = list(works)
    works.sort(key = lambda x : (-x[0], -x[1]))
    works = deque(works)
    maxDay -= 1

  return ans



print(_13904())