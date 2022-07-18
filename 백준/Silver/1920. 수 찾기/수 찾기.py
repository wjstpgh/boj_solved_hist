n=int(input())
a=sorted(list(map(int,input().split())))
m=int(input())
x=list(map(int,input().split()))

def search(a,x):
    s=0
    e=len(a)-1
    while s<=e:
        m=(s+e)//2
        if a[m]<x:
            s=m+1
        elif a[m]>x:
            e=m-1
        elif a[m]==x:
            return print(1)
    print(0)
m=a[-1]
n=a[0]
for t in range(len(x)):
    if (x[t]<=m)&(x[t]>=n):
        search(a,x[t])
    else:
        print(0)
