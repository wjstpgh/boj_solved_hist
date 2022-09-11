import sys
from collections import deque
dq=deque()

n=int(sys.stdin.readline())
for _ in range(n):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='push_front':
        dq.appendleft(cmd[1])
    elif cmd[0]=='push_back':
        dq.append(cmd[1])
    elif cmd[0]=='pop_front':
        try:
            print(dq.popleft())
        except:
            print(-1)
    elif cmd[0]=='pop_back':
        try:
            print(dq.pop())
        except:
            print(-1)
    elif cmd[0]=='size':
        print(len(dq))
    elif cmd[0]=='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=='front':
        try:
            print(dq[0])
        except:
            print(-1)
    elif cmd[0]=='back':
        try:
            print(dq[len(dq)-1])
        except:
            print(-1)