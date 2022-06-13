

n,k,i=map(int,input().split())
#마법의 돌 사전순으로 정렬
stone_list=[['I']*n for x in range(1)]

#i번째 마법의 돌 출력
def main(i,n):
    #i가 리스트 범위를 벗어났다면
    if(i>2**n):
        print('NO SUCH STONE')
    else:
        #마법의 돌 사전
        if(i>stone_add(stone_list,n,i)):
            print('NO SUCH STONE')
        else:
            #i번째 돌 문자열 변환
            i_stone=''.join(stone_list[i-1])
            print(i_stone)
        
#마법의 돌 사전 생성
def stone_add(stone_list,n,i):
    #append카운트
    cnt=1
    #바로 이전에 생성된 마법의 돌
    stone=stone_list[0][:]
    #조건없이 부분집합 무조건 생성
    for x in range(2**n-1):
        #리스트에 들어갈 후보 돌 생성
        stone=ch_XI(stone[:])
        #대칭중복조건 통과한 돌 리스트 추가
        if(ch_turn(stone_list,stone)):
            #k-조건이 통과한 돌
            if(ch_k(stone,k)):
                stone_list.append(stone)
                cnt+=1
                #i번째 리스트를 생성하면 반복문 종료
                if(cnt>=i):
                    break
            #대칭중복 불 충족시 리스트추가없이 다음 돌 생성
            else:
                continue
        #k-조건 불충족 시 리스트추가없이 다음 돌 생성
        else:
            continue    
    print(cnt)
    return cnt
        

#I를 만나면 X로 변경하고 뒤의 문자를 I로 모두 변경
def ch_XI(stone):
    #I를 만날때까지 뒤 인덱스 부터 반복
    for x in range(len(stone)):
        if(stone[-(x+1)]=='I'):
            #I를 만나면 X로 변경
            stone[-(x+1)]='X'
            #변경된 곳의 바로 뒤부터 끝까지 I로 변경
            if(x!=0):
                #x가 0이면 배열이 다 지워질뿐더러 
                #마지막 문자가 X로 변할땐 뒤를 I로 바꿔줄 필요도 없다
                stone[-x:]=['I']*x
            break
    return stone

#XI의 경계가 k개 이하인지 확인
def ch_k(stone,k):
    #k경계 카운터
    cnt=0
    for x in range(len(stone)-1):
        #배열 원소를 순회하며 경계를 검출
        if(stone[x]!=stone[x+1]):
            cnt+=1
            if(cnt>k):
                return False
    #검출된 경계수가 k이하일때 참 리턴
    return True
    
#stone이 대칭성의 중복인지 확인
def ch_turn(stone_list,stone):
    #대칭 돌 임시 생성
    reversed_stone=list(reversed(stone))
    #돌 사전 리스트에 대칭되는 형태가 있는 지 확인
    for x in range(len(stone_list)):
        if(stone_list[x]==reversed_stone):
            #대칭 형태 발견 시 거짓 반환
            return False
    #리스트에 대칭 형태 없을 시 참 반환
    return True

#main함수 실행 
main(i,n)




