k,n=map(int,input().split())
lans=[]
for x in range(k):
    lans.append(int(input()))

s,e=1,max(lans)
while s<=e:
    cnt=0
    m=(s+e)//2
    for lan in lans:
        cnt+=(lan//m)
    if cnt>=n:
        s=m+1
    else:
        e=m-1
print(e)