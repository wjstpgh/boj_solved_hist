a=input().split()
if a==sorted(a):
    print('ascending')
elif a==list(reversed(sorted(a))):
    print('descending')
else:
    print('mixed')