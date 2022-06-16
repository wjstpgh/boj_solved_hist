dice=list(map(int,input().split(' ')))

reward=0
cnt=0
same=dice[0]
big=dice[0]

for x in range(3):
    if(dice[x-1]==dice[x]):
        cnt+=1
        same=dice[x]
    elif(big<dice[x]):
        big=dice[x]
    
if(cnt==3):
    reward=10000+same*1000
elif(cnt==1):
    reward=1000+same*100
else:
    reward=big*100

print(reward)