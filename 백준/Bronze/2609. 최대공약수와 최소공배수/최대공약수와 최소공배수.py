#유클리드 호제법
a,b=map(int,input().split())
#최대공약수 함수
def gcd(a,b):
    #b의 자리에 들어오는 a를 b로 나눈 나머지가 0으로 떨어지면
    #a를 리턴, 아니라면 자리를 바꿔 재귀함수 호출
    return gcd(b,a%b) if b else a

#최대공약수
m=gcd(a,b)
print(m)
#필수인자를 가진 최대공약수가 a,b에 중첩되므로 두 수 곱하여 나눠줌
print(a*b//m)
