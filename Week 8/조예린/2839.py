def _2839() :
  N = int(input())

  # if N%5==0 : print(int(N/5))

  DP = [0]*5001
  DP[1] = 0
  DP[2] = 0
  DP[3] = 1 
  DP[4] = 0
  DP[5] = 1

  for n in range(6, N+1) :
    get3 = DP[n-3] # 3kg을 추가할 수 있을까?
    # DP[n-3] : 상근이가 (n-3)kg을 배달할 때의 봉지 최소 갯수
    # 아~ 추가할 수 있고 그때 봉지 1개를 썼네
    get5 = DP[n-5] # kg5
    # DP[n-5]==0 5kg을 추가할 수 있을까? 못함.
    # 
    if get3 == 0 and get5 == 0 :
      DP[n] = 0
    elif get3 == 0 :
      DP[n] = DP[n-5]+1
    elif get5 == 0 :
      DP[n] = DP[n-3]+1
    else :
      DP[n] = min(DP[n-3]+1, DP[n-5]+1)
  
  if DP[N] == 0 :
    print("-1")
  else :
    print(DP[N])

_2839()
