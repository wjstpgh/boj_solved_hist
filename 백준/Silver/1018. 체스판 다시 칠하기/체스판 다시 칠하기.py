#색칠수 구하기
def chColor(chess):
    cnt=0
    for x in range(64):
        xFlag=(x//8)
        if (x+xFlag)%2==0:
            flag='W'
        elif (x+xFlag)%2==1:
            flag='B'
        if chess[x]==flag:
            cnt+=1
    if cnt>32:
        cnt=64-cnt
    return cnt

n,m=map(int,input().split())
board=[]
#보드생성
for x in range(n):
    board.append(list(input()))
    
chess=''
cnt_arr=[]
#보드 잘라내기
for x in range(m-7):
    for y in range(n-7):
        for z in range(8):
            #각 잘라진 행을 문자열에 추가
            chess+=''.join(board[y+z][x:x+8])
        #색칠해야 할 수 구해서 배열에 추가
        cnt_arr.append(chColor(chess))
        chess=''

print(min(cnt_arr))