#ctrl+/ : 주석 설정
#변수 : 데이터를 저장하기 위한 공간
#변수명 : 저장된 데이터를 접근하기 위한 이름
# = :  대입연산자
# a=10
# print(a)
# a='hello python'
# print(a)
# a=3.14
# print(a)

#사칙연산 : +,-,*,/,% -> 나머지,// -> 몫
a=50
b=3
print('a=50 b=3')
print('a+b =',a+b)
print('a*b =',a*b)
print('a-b =',a-b)
print('a%b =',a%b)
print('a//b =',a//b)
# 소수점 나타내는 round 와 % 방법
print('a/b=',round(a/b, 3)  )
print('a/b=%.3f'%(a/b))
#실습)시분초 구하기
s=10000
t=s//3600
print(t,'시간')
r = s %3600
m = r//60
print(m,'분')
n = r%60
print(n,'초')

#포맷문자열
# d = 정수, f = 소수점까지
#30+20=50
a=30; b=20
print(a,'+',b, '=', a+b) #일반적인 문자
print('%d + %d = %d'%(a,b,a+b)) #포맷문자사용 예시
print('%d - %d = %d'%(a,b,a-b))
print('%d / %d = %.2f'%(a,b,a/b))
print('%d * %d = %d'%(a,b,a*b))
print('%d %% %d = %.2f'%(a,b,a%b))
