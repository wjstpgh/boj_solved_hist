a=int(input())
def b():
    num=666
    while True:
        if '666' in str(num):
            yield num
        num+=1
j=1
for i in b():
    if j==a:
        print(i)
        break
    j+=1