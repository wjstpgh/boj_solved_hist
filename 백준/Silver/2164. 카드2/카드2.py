n=int(input())
card=[i+1 for i in range(n)]
top=0
bottom=n-1

while True:
    top=(top+1)%n
    bottom=(bottom+1)%n
    card[bottom]=card[top]
    if bottom==(top+1)%n:
        print(card[top])
        break
    top=(top+1)%n
