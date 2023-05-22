n=int(input())
last=0
br=0
push=[]
answer=''
for x in range(n):
    #바로 입력받은 수
    now=int(input())
    #최고 수가 나오기 전까지는 오름차순 가능
    if br==0:
        if now>last:
            answer+=('+')*(now-last)+('-')
            for t in range(last,now-1):
                push.append(t+1)
            last=now            
        #최고 수가 나오기 전까지는 이전 수의 -1까지는 가능
        elif push[-1]==now:
            answer+='-'
            push.remove(push[-1])
        else:
            print('NO')
            answer=[]
            break
    #최고 수가 나오고 난 후에는 내림차순만 가능
    elif (now<last)&(br==1):
        answer+='-'
        last=now
    #이외의 모든 경우는 스택불가처리
    else:
        print('NO')
        answer=[]
        break
    #최고 수가 나오면 조건을 변경
    if now==n:
        br=1

for c in answer:
    print(c)