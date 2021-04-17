stairs = int(input())
number = [0 for _ in range(301)] 
summ = [0 for _ in range(301)]
for i in range(stairs):
    number[i] = int(input())
summ[0] = number[0]
summ[1] = number[0] + number[1]
summ[2] = max(number[0] + number[2],number[1] + number[2])
for i in range(3,stairs):
    summ[i] = max(number[i] + number[i-1] + summ[i-3], number[i] + summ[i-2])
print(summ[stairs-1])