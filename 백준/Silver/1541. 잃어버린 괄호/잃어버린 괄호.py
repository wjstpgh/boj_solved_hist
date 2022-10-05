sik=input()
def das(arr):
    return sum(map(int,arr.replace('-','+').split('+')))
try:
    #첫번째 마이너스기호를 기준으로 문자열 나누기
    div=sik.index('-')
    #나눠진 배열을 기호를 제거하여 숫자배열로 변경하여 합
    print(das(sik[:div])-das(sik[div+1:]))
except:
    #마이너스 기호가 없을 시 배열원소 다 더해주고 종료
    print(das(sik))