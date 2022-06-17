for x in range(3):
    a,b,c,d=map(int,input().split(' '))
    add=a+b+c+d
    if(add==0):
        print('D')
    elif(add==1):
        print('C')
    elif(add==2):
        print('B')
    elif(add==3):
        print('A')
    else:
        print('E')