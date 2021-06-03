import heapq

def _2217() :
  N = int(input())

  ropes = []
  for _ in range(N) :
    rope = int(input())
    heapq.heappush(ropes, -rope)

  total = 0
  len = 0

  while ropes :
    len += 1
    TEMP = (-1)*heapq.heappop(ropes)
    if total < TEMP*len :
      total = TEMP*len

  print(total)
  return  

_2217()
