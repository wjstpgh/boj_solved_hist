t=int(input())
for _ in range(t):
    h,w,n=map(int,input().split())
    #층수 구하기
    f=n%h
    #호수 구하기
    num=n//h+1
    if f==0:
        f=h
        num-=1
    print(f'{f}{num:02d}')
