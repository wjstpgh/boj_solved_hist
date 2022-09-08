t=int(input())
for _ in range(t):
    cnt=0
    ps=input()
    for i in ps:
        if i=='(':
            cnt+=1
        elif i==')':
            cnt-=1
        if cnt<0:
            break
    if cnt==0:
        print('YES')
    else:
        print('NO')