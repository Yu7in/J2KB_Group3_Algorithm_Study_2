import sys
k = int(sys.stdin.readline())
stck = list()
sum = 0

for _ in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        stck.pop()
    else:
        stck.append(num)
        # print(stck)

for _ in range(len(stck)):
    sum += int(stck.pop())

print(sum)
