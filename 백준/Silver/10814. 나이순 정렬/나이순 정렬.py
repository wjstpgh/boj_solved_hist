n=int(input())
boj=[]
for i in range(n):
    age,name=input().split()
    boj.append([int(age),name])

boj.sort(key=lambda x:x[0])
for i in boj:
    print(*i)
