T=int(input())
for x in range(T):
    R,S=input().split()
    for y in range(len(S)):
        print(S[y]*int(R),end='')
    print()