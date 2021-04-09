#조건문
# a=10
# #조건문 (참)
# if a>0:
#     print('양수')
#     print(a)
# #else -> 아니라면 (거짓)
# else:
#     print('음수')
#     print(a)
#
#
# print('프로그램종료')


#실습) 회원 등급을 출력
#a가 90보다 크면 good 아니면 try 출력

# 내답안지

# a=int(input("값을 입력하시오"))
#
# if a>90:
#     print('good')
# else:
#     print('try')
#

#실습 비밀번호 체크
#비밀번호가 일치하면 문이 열립니다,
#틀렸으면 '다시확인하세요'
#내 답변

# pw=int(input("비밀번호를 눌러주세요"))
#
# if pw==1234:
#     print("문이 열립니다.")
# else:
#     (input("다시 입력하세요"))


#선생님 답지

# pw=1234
# inpw=int(input('비밀번호를눌러주세요'))
#
# if pw==inpw:
#     print('문이열립니다')
# else:
#     print("다시확인하세요")
#


# 어떤수가 짝수이면 '짝수' 어떤수가 홀수이면"홀수"

# a=int(input("숫자는?"))
# if a==0:
#     print("짝수도 홀수도 아닙니다.")
# elif (a%2==0):
#     print("짝수")
# else:
#     print("홀수")


#실습) 100~90점 이상은 A,80~89 B,70~79 C,60~69 D
# 59점 이하 F
#내 답변
# a=int(input("점수를 입력하시오"))
#
# if a>=90:
#     print("A")
# elif a>=80:
#     print("B")
# elif a>=70:
#     print("C")
# elif a>=60:
#     print("D")
# elif a<=59:
#     print("F")

#실습) 몸무게와 키를 입력 받아서 비만 여부  출력
# 내답안

# height=int(input("키를 입력하시오"))
# weight=int(input("몸무게를 입력하시오"))
# normal=(height-100)*0.9
#
# if normal*0.95>weight:
#     print("미달.")
# elif normal*0.95<weight:
#     print("초과.")
# else:
#     print("정상.")


#선생님 답안
# weight=60.1
# height=165.5
# normal=(height-100)*0.9
# print('정상체중:',normal)
# if weight < normal*0.95:
#     print("미달")
# elif weight > normal*0.95:
#     print("정상")
# else:
#     print("비만")

#실습)계산기 + - / *
# 30 + 20 = 50, 두 수와 기호를 입력받아 사칙연산

# a=int(input("숫자를입력하세요"))
# b=input("기호를 입력하세요")
# c=int(input("숫자를입력하세요"))
#
# if b=='+':
#     print(a+c)
# elif b=='-':
#     print(a-c)
# elif b=='*':
#     print(a*c)
# elif b=='/':
#     print(a/c)
# else:
#     print("잘못된기호")

#2 번쨰 선생님 방법
# data=input("계산기").split()
# print(data)
# a=int(data[0])
# b=int(data[2])
# sign=data[1]
# if sign=='+':
#     print('%d + %d = %d'%(a,b,a+b))
# elif sign=='-':
#     print('%d - %d = %d'%(a,b,a-b))
# elif sign=='*':
#     print('%d * %d = %d'%(a,b,a*b))
# elif sign=='/':
#     print('%d / %d = %d'%(a,b,a/b))
# else:
#     print('잘못된 계산법')


# 내가 했던 방법
# if sign=='+':
#     print(a+b)
# elif sign=='-':
#     print(a-b)

# 다른 방법
import os
#print(os.listdir())

# data=input("계산식은?")
# # cal=eval(data)
# print(eval(data))

#실습)두 수를 입력 받아서 큰수를 화면에 출력

# a=int(input('first'))
# b=int(input('second'))
#
# if a>b:
#     print(a)
# elif a<b:
#     print(b)
# elif a==b:
#     print("숫자가 같습니다.")
# else:
#     print("다시 입력하세요")

#pos 기 실습 - 내 답지
# a=int(input('물건 값'))
# b=int(input('내신 돈'))

# if a>b:
#     print('거스름돈은',a-b,'입니다.')
# elif a<b:
#     print('돈이',a-b,'만큼 부족합니다.')
# elif a==b:
#     print('계산완료')

# 선생님답지
# amount=int(input('물건값'))
# pay = int(input('지불값'))
# if pay>amount:
#     print('거스름돈은',pay-amount,'입니다.')
# elif pay<amount:
#     print('금액이',amount-pay,'만큼 부족합니다')
# else:
#     print('계산완료')

#논리연산자
# a=10;b=20;
# print(a>0 and b>0)
# print(a>0 and b<0)
# print(a>0 or b<0)
# print(not(a>0))

# a=-10;b=-4
#
# if a==0 or b==0:
#     print('0이 아닌 수를 입력하세요')
# elif a>0 and b>0:
#     print('둘다 양수')
# elif a>0 or b>0:
#     print('둘중 하나는 음수')
# else:
#     a<0 and b<0
#     print('둘다 음수')

#실습
price = ({'1':['자장면', 5000,'중식'],'2':['짬뽕', 6000,'중식'], '3':['설렁탕',8000,'한식'],
         '4':['비빔밥', 10000,'한식'], '5':['피자',12000,'양식'],'6':['스파게티',9000,'양식']})
print(price)
print('1.자장면\n2.짬뽕\n3.설렁탕\n4.비빔밥\n5.피자\n6.스파게티')
print('-'*20)
no = input('선택하세요')
menukey = price.keys()
if no in menukey:
    print(price[no][0],'선택')
    print(price[no][1],'원')
    print(price[no][2],'코너')#if 없이도 가능
else:
    print('다시입력하세요')
# if not no in ['1','2','3','4','5','6']:
#     print('다시입력하세요')
# if no in ['1','2']: #in : 포함여부
#     print('중식코너로 가세요')
# elif no in ['3','4']:
#     print('한식코너로 가세요')
# elif no in ['5','6']:
#     print('양식코너로 가세요')
# else:
#     print('다시 입력해주세요')

#2)