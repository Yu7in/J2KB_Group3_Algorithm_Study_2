people = int(input(""))
time = list(map(int,input().split()))
time.sort()
each_time = 0
total_time = 0
for i in time:
    each_time += i
    total_time += each_time
print(total_time)