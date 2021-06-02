import sys
input = sys.stdin.readline

N = int(input())
ropes = []
answer = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort(reverse=True)

for i in range(N):
    answer.append(ropes[i]*(i+1))

print(max(answer))


