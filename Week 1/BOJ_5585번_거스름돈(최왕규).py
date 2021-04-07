# BOJ_5585번_
coinList = [500,100,50,10,5,1]

sum_money = 1000
remainder = int(input(''))

sum_money = sum_money - remainder
count = 0

for i in coinList:
    while sum_money>=i:
        sum_money = sum_money - i
        count = count + 1

print(count)

        


