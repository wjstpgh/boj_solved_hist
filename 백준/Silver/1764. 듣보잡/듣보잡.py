import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dic={}
for _ in range(n):
    dic[input().rstrip()]=0
arr=[]
for _ in range(m):
    try:
        a=input().rstrip()
        dic[a]
        arr.append(a)
    except:
        pass
print(len(arr))
arr.sort()
for i in arr:
    print(i)