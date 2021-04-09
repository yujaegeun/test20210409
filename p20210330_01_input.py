#사용자에게 입력 받기
# a=input('이름은?')
# print('입력한 값은',a)

#실습 ( 나이를 입력받아 화면에 출력 )
#입력한 값은 문자취급
# b=input('당신의 나이는')
# print('당신의 나이는',b,'살 입니다.',sep='')

# 날씨를 입력받아 오늘의 날씨 출력
# txt = '오늘의 날씨는'
# c = input('날씨 :')
# print(txt,c,sep='*')

#도움말 출력
#help(print)
#help(input)


#사용자가 입력한 값에 100을 더해서 출력

# a=input('숫자 입력')
# a=int(a) #int 정수로 변환해서 반환 해주는 함수
# a=float(a) #float 실수로 변환해서 반환해주는 함수
# print('나온값',a+100)


#실습)  사용자에게 두 수를 입력 받아 사친연산 프로그램 계산기
 # 내 답안지
# a=input("첫번째 숫자를 입력하세요")
# b=input("두번째 숫자를 입력하세요")
#
# a=int(a)
# b=int(b)
#
# print("곱한값",a*b)
# print("더한값",a+b)
# print("빼기",a-b)
# print("나누기",a/b)

#1번 - 교수님 답안지
# a= int(input('첫번째수?'))
# b= int(input('두번째수?'))
# print('%d + %d = %d'%(a,b,a+b))
# #print('두 수를 더한 값은',a+b, '입니다')
# print('%d - %d = %d'%(a,b,a-b))
# print('%d * %d = %d'%(a,b,a*b))
# print('%d / %d = %d'%(a,b,a/b))

# data=input('두수는?')
# a=int(data.split()[0])
# b=int(data.split()[1])
#
# print(a,'+',b,'=',a+b)

#2
# data = input('두수는?').split() #두수를 분리
# a,b=list(map(int,data)) #map 함수는 data의 각 값을 int함수를 적용해서 a,b에 대입
# print(a,'+',b,'=',a+b)

#실습) 반지름 구하기 - 내 답변
# a=int(input("반지름의 길이는?"))
# b=3.14
# b=float(b)
# print('원의 넓이는',a*a*b ,'입니다.')

#선생님 답안
#a=int(input('반지름:'))
a=float(input('반지름'))
print('원의 넓이는',a*a*3.14) # **두개는 제곱의미

