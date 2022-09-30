n=int(input())
m=int(input())
if m:#고장난 버튼이 있을때
    btn=list(input().split())
    #클릭 가능한 채널인지 확인
    def notBroke(chn):
        for c in chn:
            if c in btn:
                return False
        return True
else:#고장난 버튼이 없을때 모든 수 클릭가능
    def notBroke(chn):
        return True
#기본 채널에서 결과까지 숫자버튼없이 가는 클릭수
cnt=abs(100-n)
#0부터 100000까지의 모든 수가 클릭가능한지 확인하고 클릭수구하기
for chn in range(int(1e6)+1):
    c=str(chn)
    if notBroke(c):
        cnt=min(cnt,len(c)+abs(n-chn))
print(cnt)