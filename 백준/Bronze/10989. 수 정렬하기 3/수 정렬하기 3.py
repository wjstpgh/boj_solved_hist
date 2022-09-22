import sys
input = sys.stdin.readline
n=int(input())
d={}
for _ in range(n):
    if(i:=int(input())) in d.keys():
        d[i]+=1
    else:
        d[i]=1
d=sorted(d.items())

for k,v in d:
    for _ in range(v):
        print(k)