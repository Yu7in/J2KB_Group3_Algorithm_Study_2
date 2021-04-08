N = int(input(""))
count = 0
number = 0
for i in range(5):
    if (N%5 == 0 and N >= 0):
        count += N//5
        print(count)
        exit()
    N -= 3
    count += 1 
if N < 0:
    print("-1")