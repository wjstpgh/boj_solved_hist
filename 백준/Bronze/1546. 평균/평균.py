N=int(input())
score=list(map(float,input().split()))
M=max(score)
for x in range(N):
    score[x]=score[x]/M*100
print(sum(score)/N)