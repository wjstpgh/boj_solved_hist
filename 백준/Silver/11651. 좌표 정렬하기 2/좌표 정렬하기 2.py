n=int(input())
dot=[]
for _ in range(n):
    dot.append(list(map(int,input().split())))
dot.sort(key=lambda x:(x[1],x[0]))
for i in dot:
    print(*i)