money = int(input())

coins = [500, 100, 50, 10, 5, 1]
change = 1000-money
ans_cnt = 0

for c in coins:
    cnt = 0
    # print(change, c, cnt, ans_cnt)
    cnt += change // c
    change -= c*cnt
    ans_cnt += cnt
    # print(change, c, cnt, ans_cnt)

print(ans_cnt)