import sys

input = sys.stdin.readline

# 입력
X = int(input())

table = [0 for _ in range(X + 1)]


'''
1 : 1 
2 : 2 - 1 
3 : 3 - 1 , 3 - 2 - 1
4 : <4 - 2 - 1> , 4 - 3 - 1
5 : 5 - 4 - 2 - 1 
6 : <6 - 2 - 1> , 6 - 5 - 4 - 2 - 1
7 : 7 - 6 - 2 - 1 
8 : <8 - 4 - 2 - 1> , 8 - 7 - 6 - 2 - 1
9 : <9 - 3 - 1 >, 9 - 8 - 4 - 2 - 1
10 : <10 - 9 - 3 - 1> , 10 - 5 - 4 - 2 - 1


'''
for i in range(1, X + 1):
    if i == 1:
        table[i] == 0
    else:
        table[i] = table[i - 1] + 1
        if i % 3 == 0:
            table[i] = min(table[i], table[i // 3] + 1)
        if i % 2 == 0:
            table[i] = min(table[i], table[i // 2] + 1)

# 출력은 1이 나올때까지 받는 최소 횟수
print(table[X])
