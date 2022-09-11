def fac(num):
    fac=1
    for x in range(2,num+1):
        fac*=x
    return fac

n,k=map(int,input().split())
print(fac(n)//(fac(k)*fac(n-k)))