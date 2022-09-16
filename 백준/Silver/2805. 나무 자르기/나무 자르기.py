import sys
input=sys.stdin.readline
n,m=map(int,input().split())
tree=list(map(int,input().split()))
s,e=0,max(tree)
def funckin_python(s,e):
    while s+1<e:
        cnt=0
        mid=(s+e)//2
        for i in tree:
            if mid<i:
                cnt+=(i-mid)
        if cnt<m:
            e=mid
        else:
            s=mid
    print(s)

funckin_python(s, e)