import heapq, sys
input=sys.stdin.readline
hq=[]
n=int(input())
for _ in range(n):
    x=int(input())
    if x:
        heapq.heappush(hq, x)
    elif not x:
        try:
            print(heapq.heappop(hq))
        except:
            print(0)