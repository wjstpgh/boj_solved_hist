m=int(input())
li=sorted(list(map(int,input().split())))
n=li[-1]+1
s=li[0]
if s==1:
    s=2
end=int(n**.5)
num=[True]*n

for i in range(2,end+1):
    if num[i]==True:
        for x in range(i*2,n,i):
            num[x]=False

ans=[i for i in range(s,n) if num[i]==True]

cnt=0
for a in li:
    if a in ans:
        cnt+=1

print(cnt)


