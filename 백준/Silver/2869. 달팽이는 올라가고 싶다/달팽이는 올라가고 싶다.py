a,b,v=map(int,input().split())

day=(v-b)//(a-b)
if (v-b)%(a-b):
    day+=1
print(day)