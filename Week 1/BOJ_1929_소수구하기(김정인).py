import sys

m,n=map(int,sys.stdin.readline().split())

for i in range(m,n+1):
    for j in range(2,(i//2)+2):
        if j==(i//2)+1:
            print(i)
        elif i%j==0:
            break