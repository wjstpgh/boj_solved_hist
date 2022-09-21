k=int(input())
num=[]
for _ in range(k):
    i=int(input())
    if i==0:
        del num[-1]
    else:
        num.append(i)
print(sum(num))