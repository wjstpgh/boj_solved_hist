n=int(input())
answer=0
for x in range(n):
    if x+sum(list(map(int,str(x))))==n:
        answer=x
        break
print(answer)  
