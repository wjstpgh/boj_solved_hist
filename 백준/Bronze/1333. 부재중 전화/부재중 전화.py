N,L,D=map(int,input().split(' '))

def alarm(N,L,D):
    time=0
    if(D<=5):
        time=D
        while(time<L):
            time+=D
        return time
    for x in range(N):
        time+=(L+5)
        if(time//D!=0 & 0<time%D<6):
            time-=time%D
            return time
    L=time
    time=D
    while(time<L):
        time+=D
    return time

print(alarm(N,L,D))