import sys

input = sys.stdin.readline

price = int(input())

remainder = 1000 - price

coin = [0] * 6

while remainder > 0:
    if remainder // 500 >= 1:
        coin[0] += remainder // 500
        remainder %= 500
    elif remainder // 100 >= 1:
        coin[1] += remainder // 100
        remainder %= 100
    elif remainder // 50 >= 1:
        coin[2] += remainder // 50
        remainder %= 50
    elif remainder // 10 >= 1:
        coin[3] += remainder // 10
        remainder %= 10
    elif remainder // 5 >= 1:
        coin[4] += remainder // 5
        remainder %= 5
    elif remainder // 1 >= 1:
        coin[5] += remainder // 1
        remainder %= 1

print(sum(coin))
