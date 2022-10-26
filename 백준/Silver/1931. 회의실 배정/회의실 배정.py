n=int(input())
meet=[]
for _ in range(n):
    meet.append(tuple(map(int,input().split())))
#끝시간을 우선으로 정렬해서 일전회의의 끝시간보다
#시작, 끝 시간 모두 이후인 회의만 카운트
meet.sort(key=lambda x:(x[1],x[0]))
last=meet[0][1];cnt=1
for i in range(1,n):
    if meet[i][0]>=last:
        cnt+=1
        last=meet[i][1]
print(cnt)