n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]
cnt=[0]*3

def cut(x,y,n):
    num=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if num!=paper[i][j]:
                n//=3
                for t in range(3):
                    for r in range(3):
                        cut(x+n*t,y+n*r,n)
                return
    cnt[num+1]+=1

cut(0,0,n)
print(*cnt,sep='\n')