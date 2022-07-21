m,n=map(int,input().split())
if m==1:
    m=2
n+=1

num=[True]*n
end=int(n**0.5)
for x in range(2,end+1):
    if num[x]==True:
        for y in range(x*2,n,x):
            num[y]=False

for x in range(m,n):
    if num[x]==True:
        print(x)