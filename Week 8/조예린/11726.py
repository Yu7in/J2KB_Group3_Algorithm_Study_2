def _11726() :
  
  dp = [0]*1001
  dp[1] = 1
  dp[2] = 2

  N = int(input())
  for n in range(3, N+1) :
    dp[n] = (dp[n-1] + dp[n-2])%10007

  print(dp[N])

_11726()
