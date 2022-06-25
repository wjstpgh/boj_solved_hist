L=int(input())
S=list(map(int,input().split(' ')))
n=int(input())

if n in S:
    print(0)
else:
    S.append(n)
    S.sort()
    idx_n=S.index(n)
    if(idx_n==0):
        print((n)*(S[idx_n+1]-n)-1)
    else:
        print((n-S[idx_n-1])*(S[idx_n+1]-n)-1)