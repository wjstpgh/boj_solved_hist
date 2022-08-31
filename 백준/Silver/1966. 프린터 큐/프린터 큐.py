case=int(input())

for _ in range(case):
    n,m=map(int,input().split())
    pq=list(map(int,input().split()))
    impo=list(reversed(sorted(pq)))
    im_idx,front=0,0
    cnt=0
    while True:
        if pq[front]==impo[im_idx]:
            cnt+=1
            if front==m:
                break
            pq[front]=-1
            im_idx+=1
            
        front=(front+1)%(n)
        
    print(cnt)
