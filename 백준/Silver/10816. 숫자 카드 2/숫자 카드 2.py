def binary(d,li):
    start=0
    end=len(li)-1
    while start<=end:
        mid=(start+end)//2
        if li[mid]==d:
            return True
        elif li[mid]<d:
            start=mid+1
        else:
            end=mid-1
    return False

n=int(input())
card=map(int,input().split())
m=int(input())
num=map(int,input().split())
c={}
for card in card:
    if not card in c:
        c[card]=1
    else:
        c[card]+=1
        
s=sorted(c.keys())
for num in num:
    flag=binary(num,s)
    if flag:
        print(c[num],end=' ')
    if not flag:
        print(0,end=' ')
