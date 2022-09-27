def bechew(x,y):
    #좌표를 벗어나거나 배추가 없으면 함수종료
    if (x<0) | (y<0) | (x>=m) | (y>=n):
        return
    elif not baat[y][x]:
        return
    #해당좌표배추체크 후 인접배추체크 반복
    baat[y][x]=0
    bechew(x+1,y)
    bechew(x-1,y)
    bechew(x,y+1)
    bechew(x,y-1)

t=int(input())
for _ in range(t):
    #가로, 세로, 배추갯수
    m,n,k=map(int,input().split())
    #밭은 가로m에 세로n의 2차배열
    baat=[[0]*m for _ in range(n)]
    #배추심기
    for _ in range(k):
        x,y=map(int,input().split())
        baat[y][x]=1
    #배추뭉치 체크후 지렁이 투하
    zirung=0
    for x in range(m):
        for y in range(n):
            if baat[y][x]==1:
                bechew(x,y)
                zirung+=1
    print(zirung)