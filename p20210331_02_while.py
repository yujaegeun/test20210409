#반복문 : while
#조건이 참일 동안 실행
# while True:
#     print('python')

# a=0
# while a<10:
#     a += 1
#     print(a)

# #실습 1~10까지 합을 출력
# a=0 # 합계를 누적 할 변수
# b=0  # 증가하는 변수
# while True:
#     b+=1
#     if b>10:break
#     a += b
# print(a)

#a가 증가하면서 누적합계를 구하고 그 합계가 2000이 넘으면 종료
# s=0 #합계변수
# a=0 #증가변수
# while True:
#     a+=1
#     s+=a
#     if s<2000:
#         print(a,s)
#2)
# s=0
# a=0
# while s<2000:
#     a+=1
#     s+=a
# print(a,s)

#사용자가 입력한 수를 누적 하다가
# 만약 0을 입력하면 종료 후 누적 합계를 출력
#1)
# s=0
# while True:
#     a=int(input("더할 값은?"))
#     if a==0:break
#     s+=a
# print("합계는",s,'입니다.')

#2
# s=0
# a=1
# while a!=0:
#     a=int(input('더할 값은?'))
#     s+=a
# print(s)

