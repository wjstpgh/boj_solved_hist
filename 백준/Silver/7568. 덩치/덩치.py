n=int(input())
man=[]
for x in range(n):
    man.append(list(map(int,input().split())))
    
rank=[]
for x in man:
    cnt=1
    for y in man:
        if (x[0]<y[0]) & (x[1]<y[1]):
            cnt+=1
    rank.append(cnt)

print(*rank)