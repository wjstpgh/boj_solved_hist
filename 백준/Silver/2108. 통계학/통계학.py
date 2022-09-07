import sys
n=int(sys.stdin.readline())
li=[]
cnt={}
avg=0
for _ in range(n):
    num=int(sys.stdin.readline())
    avg+=num
    li.append(num)
    if num not in cnt:
        cnt[num]=1
    else:
        cnt[num]+=1

many=max(list(cnt.values()))
many_li=[key for key in cnt if cnt[key]==many]
li.sort()
many_li.sort()

print(round(avg/n))
print(li[(n-1)//2])
if len(many_li)==1:
    print(many_li[0])
else:
    print(many_li[1])
print(li[-1]-li[0])