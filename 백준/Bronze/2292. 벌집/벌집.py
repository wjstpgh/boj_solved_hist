n=int(input())

#1번 방에서 시작
cnt=1
#중심1부터 각 층의 마지막 수,1층부터 시작
num=1
#층의 마지막 수가 n을 넘길때 까지 반복
while n>num:
    num+=(6*cnt)
    cnt+=1

print(cnt)
