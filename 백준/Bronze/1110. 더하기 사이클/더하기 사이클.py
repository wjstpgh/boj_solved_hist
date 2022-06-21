N=int(input())
def nextNum(num):
    if(num<10):
        num*10
    newOne=((num//10)+(num%10))%10
    newTen=num%10
    return (newTen*10)+newOne
new=nextNum(N);cycle=1
while(N!=new):
    new=nextNum(new)
    cycle+=1
print(cycle)