n,y,x=map(int,input().split())
cnt=0#방문횟수
#차수가 하나씩 줄어들며 사분면 찾아가기
for d in reversed(range(n)):
    line=2**d#현재 사분면의 기준선 크기
    dum=line**2#한 사분면의 크기
    if y>=line:
        if x>=line:#4사분면
            cnt+=dum*3
            x-=line
            y-=line
        else:#3사분면
            cnt+=dum*2
            y-=line
    else:
        if x>=line:#2사분면
            cnt+=dum
            x-=line
        else:#1사분면
            pass
print(cnt)