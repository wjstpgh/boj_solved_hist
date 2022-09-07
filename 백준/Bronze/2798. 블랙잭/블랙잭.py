n,m=map(int,input().split())
card=list(map(int,input().split()))

zack=0
for x in range(0,n-2):
    for y in range(x+1,n-1):
        for z in range(y+1,n):
            card_sum=card[x]+card[y]+card[z]
            if zack<card_sum and card_sum<m:
                zack=card_sum
            elif card_sum==m:
                zack=card_sum
                break
print(zack)
