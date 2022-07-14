import string
atoz=list(string.ascii_lowercase)
s=input()
for c in atoz:
    try:
        print(s.index(c),end=' ')
    except:
        print(-1,end=' ')