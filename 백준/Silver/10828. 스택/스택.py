import sys
stack=[]

n=int(sys.stdin.readline())
for _ in range(n):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='push':
        stack.append(cmd[1])
    elif cmd[0]=='pop':
        try:
            print(stack[len(stack)-1])
            del stack[len(stack)-1]
        except:
            print(-1)
    elif cmd[0]=='size':
        print(len(stack))
    elif cmd[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=='top':
        try:
            print(stack[len(stack)-1])
        except:
            print(-1)