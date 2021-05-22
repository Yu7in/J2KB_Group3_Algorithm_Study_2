# N : 물품의 수
# K : 준서가 버틸 수 있는 무게
# W V : 무게, 가치
# 배낭에 최대한 가치있게 넣기

# 사용 알고리즘 : DP -> 0-1 배낭문제(0-1 Knapsak Problem)
#   - 담을 수 있는 물건이 나누어질 수 없을 때(담거나 or 담지 않거나) 사용하는 DP 기법

def _12865() :
  N, K = map(int, input().split())
  goods = [[0,0]]
  for _ in range(N) :
    W, V = map(int, input().split())
    goods.append([W,V])
  
  knapsack = [[0]*(K+1) for _ in range(N+1)]
  
  for i in range(1,N+1) : # num
    for j in range(1,K+1) : # temp_weight
      (w, v) = goods[i]
      if j < w : # 현재 물건을 담을 수 없는 경우에는
        knapsack[i][j] = knapsack[i-1][j] # 이전 상태를 유지
      else :
        # 담을 수 있는 경우에는, 현재 무게를 담은 상태와 이전 상태 중 큰 것을 저장한다
        knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])
  
  print(knapsack[N][K])



_12865()
