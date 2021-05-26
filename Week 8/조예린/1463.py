def _1463() :
  N = int(input())
  dp = [0]*(10**6+1)

  dp[1] = 0
  dp[2] = 1
  dp[3] = 1

  for n in range(4, N+1) :
    if n%2 == 0 and n%3 == 0 :
      dp[n] = min(dp[n-1], dp[int(n/2)], dp[int(n/3)])
    elif n%2 == 0 :
      dp[n] = min(dp[n-1], dp[int(n/2)])
    elif n%3 == 0 :
      dp[n] = min(dp[n-1], dp[int(n/3)])
    else :
      dp[n] = dp[n-1]
    dp[n] += 1

  print(dp[N])

_1463()
