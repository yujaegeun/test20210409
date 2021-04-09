#모듈

# import time
# print(time.localtime().tm_year,'년',time.localtime().tm_mon,'월',time.localtime().tm_hour,'시',time.localtime().tm_min,'분',time.localtime().tm_sec,'초',end='')
# print(time.localtime().tm_year,'년')
# print(time.localtime().tm_mon,'월')
# print(time.localtime().tm_hour,'시')
# print(time.localtime().tm_min,'분')
# print(time.localtime().tm_sec,'초')

# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.strftime('%Y-%m-%d %H:%M:%S'))

# from datetime import datetime
# now =datetime.now()
# print(now)
# print(now.strftime('%Y-%m-%d %H:%M:%S'))

#time 모듈 실습
# 1초마다 화면에 타이머를 출력
# #sleep 함수 : 프로그램 실행 속도를 제어
# import time
# print('시작')
# time.sleep(3)
# print('3초지남')

#time 모듈 실습
# 1초마다 화면에 타이머를 출력
# import time
# sec = int(input('몇초'))
# print("타이머시작")
# for x in range(1,sec+1):
#     time.sleep(1)
#     print(x,"초")
# print("타이머종료")

# from time import sleep
# sec = int(input('몇초'))
# print("타이머시작")
# for x in range(1,sec+1):
#     5sleep(1)
#     print(x,"초")
# print("타이머종료")

#난수모듈
#주사위 게임
# awin=0
# bwin=0
# import random
# while True :
#     a = random.randint(1, 6)
#     b = random.randint(1, 6)
#     if a>b:awin+1
#     print('a가 이겼습니다')
#     if a<b:bwin+1
#     print('b가 이겼습니다')
#     if awin or bwin==3:
#         break

#sample()
# import random
# print(random.sample(range(1,46),6))

#choice()
# import random
# print(random.choice(['가위','바위','보']))
#
#
# #shiffle():섞는다
# data=['나비','벌','나비','벌','꽃','꽃']
# random.shuffle(data)
# print(data)

import turtle
turtle.shape('turtle')
turtle.color('red')
for x in range(8):
    turtle.forward(100)
    turtle.right(90)

turtle.done()