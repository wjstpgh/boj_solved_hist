case=int(input())

for x in range(case):
    score,cnt=0,0
    s=input()
    for y in range(len(s)):
        if(s[y]=='O'):
            cnt+=1
            score+=cnt
        else:
            cnt=0
    print(score)