import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    N = int(input())
    P = [0, 1, 1, 1]

    for i in range(4, N+1):
        P.append(P[i-3] + P[i-2])

    print(P[-1])