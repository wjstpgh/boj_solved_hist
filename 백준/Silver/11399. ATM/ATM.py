n=int(input())
p=sorted(list(map(int,input().split())))
t=0;s=0
for i in p:
   t+=i
   s+=t
print(s)