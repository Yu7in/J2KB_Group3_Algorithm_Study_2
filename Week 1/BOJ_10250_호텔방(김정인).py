#호텔 방
import sys
t=int(sys.stdin.readline())

a=[0]*t
for i in range(t):
    h,w,n=map(int,sys.stdin.readline().split())
    wide=n//h+1
    floor=n%h
    # if floor==0:
    #     floor=h
    #     wide-=1
    if (n==h*w and n/h==w) or floor==0:
        wide-=1
        floor=h
    a[i]=(floor*100)+(wide)

for i in range(t):
    print(a[i])