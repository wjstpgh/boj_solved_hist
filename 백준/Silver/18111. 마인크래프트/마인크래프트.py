n,m,b=map(int,input().split())
g=''
for _ in range(n):
    g+=input()+' '
g=list(map(int,g.split()))
time,h=0,0
for block in range(min(g),max(g)+1):
    cnt=0
    inven=b
    for ground in g:
        if ground>block:
            cnt+=(ground-block)*2
            inven+=(ground-block)
        elif ground<block:
            cnt+=(block-ground)
            inven-=(block-ground)
    if ((time==0) | (cnt<=time)) & (inven>=0):
        time=cnt
        if (h<block) | (h==0):
            h=block
print(time,h)