import sys
n=int(sys.stdin.readline())
li=[]
for _ in range(n):
    li.append(int(sys.stdin.readline()))
    
li.sort()

for x in range(n):
    print(li[x])
