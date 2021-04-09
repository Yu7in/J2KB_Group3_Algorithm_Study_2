# # 거스름돈
# import sys

# buy=int(sys.stdin.readline())

# money=1000-buy
# count=0

# if money>=500:
#     count+=1
#     money-=500

# if money>=100:
#     count+=(money//100)
#     money-=(money//100*100)

# if money>=50:
#     count+=(money//50)
#     money-=(money//50*50)

# if money>=10:
#     count+=(money//10)
#     money-=(money//10*10)

# if money>=5:
#     count+=(money//5)
#     money-=(money//5*5)

# count+=money

# print(count)

import sys

buy=int(sys.stdin.readline())

money=1000-buy

coin=[500,100,50,10,5,1]
count=0

for i in coin:
    count+=(money//i)
    money-=(money//i*i)

print(count)