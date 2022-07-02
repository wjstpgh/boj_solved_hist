serial=list(map(int,input().split()))
num=0
for x in range(len(serial)):
    num+=(serial[x]**2)
print(num%10)