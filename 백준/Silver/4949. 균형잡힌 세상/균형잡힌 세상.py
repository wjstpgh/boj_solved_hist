#풀이저장용, 입력l이 .이 아닐때까지 반복
while(l:=input())!='.':
 s=''
 #문자열 l의 원소 탐색
 for i in l:
#문자 i가 해당괄호중일때, s로 옮기며, 
#옮겨진 s에서 괄호짝이 맞는 즉시 공백으로 변환
  if i in'()[]':s=(s+i).replace('()','').replace('[]','')
  #문자열 순회 후 s가 문자가 존재한다면 부등호가 참
  #참은 1로 2번째 인덱스부터 2스탭씩 슬라이싱
  #반대로 s가 공백이라면 0으로 첫번째부터 2스탭씩 슬라이싱
 print('yneos'[s>''::2])