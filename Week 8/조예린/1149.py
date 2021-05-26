R = 0
G = 1
B = 2

def _1149() :
  N = int(input())
  house = [[0]*3 for _ in range(N)]
  
  for n in range(N) :
    house[n] = list(map(int, input().split()))

  # print(house)
  
  dp = [[0]*3 for _ in range(N)]

  # print(dp)
  # dp[n][R] : 이번에 집을 빨간 색으로 칠하는 경우
  dp[0][R] = house[0][R]
  dp[0][G] = house[0][G]
  dp[0][B] = house[0][B]

  for n in range(1, N) :
    dp[n][R] = min(dp[n-1][G], dp[n-1][B]) + house[n][R]
    dp[n][G] = min(dp[n-1][R], dp[n-1][B]) + house[n][G]
    dp[n][B] = min(dp[n-1][R], dp[n-1][G]) + house[n][B]
    # print(n, "->", dp[n])
  
  print(min(dp[N-1]))


_1149()
