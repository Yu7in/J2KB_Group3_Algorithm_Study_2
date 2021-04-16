import sys

n = sys.stdin.readline().strip()
sum_int = 0
cycle = 0
sum_n = ''
new_n = ''

if len(n) <= 1:
    n = '0' + n
chck_n = n

while chck_n != new_n:
    cycle += 1
# for _ in range(0,4):
    # print('n: ', n)

    for l in n:
        # print('l: ', l)
        sum_int += int(l)

    if sum_int < 10:
        new_n = n[-1] + str(sum_int)
    else:
        new_n = n[-1] + str(sum_int)[-1]
    # print('sum_int: ', sum_int)
    # print('new_n: ', new_n)
    n = new_n
    sum_int = 0
    # if cycle == 61:
    #     break
print(cycle)
