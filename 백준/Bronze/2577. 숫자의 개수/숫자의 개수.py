num=1
for x in range(3):
    num*=int(input())
    
for x in range(10):
    print(str(num).count('{0}'.format(x)))