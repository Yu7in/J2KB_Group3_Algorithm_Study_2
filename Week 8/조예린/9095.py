def _9095() :
  T = int(input())
  dp = [0]*(11+1)
  dp[1] = 1
  dp[2] = 2
  dp[3] = 4
  for n in range(4,12) :
    dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
  for _ in range(T) :
    N = int(input())
    print(dp[N])

_9095()
