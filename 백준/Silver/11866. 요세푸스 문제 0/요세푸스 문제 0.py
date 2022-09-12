n,k=map(int,input().split())
arr=[i for i in range(1,n+1)]

pic=[]
idx=0
k-=1

for x in range(n):
    idx=(idx+k)%len(arr)
    pic.append(arr.pop(idx))

print('<',end='')
print(*pic,sep=', ',end='')
print('>')