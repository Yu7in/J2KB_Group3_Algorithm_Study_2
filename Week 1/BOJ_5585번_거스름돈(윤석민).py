change = 1000 - int(input(""))
count = 0
coin_list = [500,100,50,10,5,1]
for i in coin_list:
    count += change//i
    change %= i
print(count)
