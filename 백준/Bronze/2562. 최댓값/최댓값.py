arr=[0]*9
for x in range(9):
    arr[x]=int(input())
print(max(arr))
print(arr.index(max(arr))+1)