while 1:
    s=input()
    if s[0]=='.':
        break
    t=[]
    for i in range(len(s)):
        if s[i]=='(':
            t.append(')')
        elif s[i]=='[':
            t.append(']')
        elif (s[i]==']') | (s[i]==')'):
            if len(t)==0:
                print('no')
                break
            else:
                if t[len(t)-1]==s[i]:
                    del t[len(t)-1]
                else:
                    print('no')
                    break
    if i+1==len(s):
        if len(t)==0:
            print('yes')
        else:
            print('no')