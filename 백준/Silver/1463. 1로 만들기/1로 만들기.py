n=int(input())
#n의 각 숫자에 따라 최솟값저장배열
cnt=[0]*(n+1)
for i in range(2,n+1):
    #1을 감소시킬때
    cnt[i]=cnt[i-1]+1
    #3으로 나누어 떨어질때
    if not i%3:
        #1감소와 3으로 나누는 것 비교
        cnt[i]=min(cnt[i],cnt[i//3]+1)
    if not i%2:
        cnt[i]=min(cnt[i],cnt[i//2]+1)
print(cnt[n])