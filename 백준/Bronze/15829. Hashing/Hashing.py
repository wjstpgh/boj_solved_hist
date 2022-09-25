l=int(input())
string=input()
h=0
for s in range(l):
    h+=(ord(string[s])-96)*(31**s)
    
print(h%1234567891)