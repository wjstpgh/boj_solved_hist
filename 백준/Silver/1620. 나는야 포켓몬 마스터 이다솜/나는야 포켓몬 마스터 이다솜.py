n,m=map(int,input().split())
dic={}
for i in range(n):
    dic[i+1]=input()
dic2=dict(map(reversed,dic.items()))
for _ in range(m):
    iors=input()
    try:
        print(dic[int(iors)])
    except:
        print(dic2[iors])