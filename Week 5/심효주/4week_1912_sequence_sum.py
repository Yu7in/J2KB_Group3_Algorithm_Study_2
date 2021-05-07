import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [arr[0]]

for i in range(n-1):
    ans.append(max(ans[i] + arr[i+1], arr[i+1]))

print(max(ans))