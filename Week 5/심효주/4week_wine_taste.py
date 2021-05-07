import sys
input = sys.stdin.readline

n = int(input())
wines = [0]
DP = [0]

for i in range(1,n+1):
    wines.append(int(input()))

DP.append(wines[1])
# DP.append(wines[1]+wines[2])

if n > 1:
    DP.append(wines[1]+wines[2])
# DP[3] = max(DP[1], DP[2]) + wines[3]

for i in range(3, n+1):
    # dp[i] = (max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i]))
    DP.append(max(DP[i-1], DP[i-3]+wines[i-1]+wines[i], DP[i-2]+wines[i]))

print(max(DP))