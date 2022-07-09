n=int(input())

for x in range(n):
    print('{0}{1}'.format(' '*(n-(x+1)),'*'*(x+1)))