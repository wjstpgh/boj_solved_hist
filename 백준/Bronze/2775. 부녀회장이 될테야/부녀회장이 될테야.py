t=int(input())

for _ in range(t):
    k=int(input())
    n=int(input())
    #0층
    arr=[i+1 for i in range(n)]
    #k층 배열 구하기
    for x in range(1,k+1):
        arr[0]=1
        for y in range(1,n):
            arr[y]+=arr[y-1]
    print(arr[n-1])