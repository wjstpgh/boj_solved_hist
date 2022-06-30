H,M=map(int,input().split())
alarm=H*60+M-45
if(alarm<0):
    alarm+=24*60
print(alarm//60,alarm%60)