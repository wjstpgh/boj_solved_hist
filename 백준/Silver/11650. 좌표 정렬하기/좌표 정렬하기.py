n=int(input())

dot=[]
for _ in range(n):
    dot.append(list(map(int,input().split())))
    
dot.sort(key=lambda x:(x[0],x[1]))

for i in dot:
    print(*i)