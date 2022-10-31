n=int(input())
img=[input() for _ in range(n)]
zp=''

def cut(x,y,n):
    global zp
    if n==1:
        zp+=img[x][y]
        return
    
    num=img[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if img[i][j]!=num:
                n//=2
                zp+='('
                for z in range(2):
                    for t in range(2):
                        cut(x+z*n, y+t*n, n)
                zp+=')'
                return
    zp+=num
    return

cut(0,0,n)
print(zp)