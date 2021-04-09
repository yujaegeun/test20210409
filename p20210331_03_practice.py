# 연습문제
# 1)별 찍기 1
# for x in range(1,6):
#     print('*' * x)

# for x in range(1,10,2):
#     print('*' * x)



# 2) 별 찍기 2
# for x in range(6,0,-1):
#     print('◑' * x)




#3)별찍기3 *과제*
# print()

# 실습 구구단
# a=2
# for x in range(1,11):
#     print(a,'*',x,'=',x*2)

# a=3
# for x in range(1,11):
#     print(a,'*',x,'=',x*3)


# a=int(input('숫자입력'))
# for x in range(1,11):
#     print('%d * %d = %d'%(a,x,a*x))
#실습 2~9단까지 동시 출력
# for x in range(2,10):
#     for y in range(1,10):
#         print('%d * %d = %d'%(x,y,x*y))


# 실습3- 수를 입력받아 그 범위안의 수 중 0부터 3의 배수
# x=int(input('숫자를 입력하세요'))
# for x in range(x,31,3):
#     print(x, end=' ')

#선생님 답변
# a = int(input('마지막 수는'))
# for x in range(0,a+1,3):
#     print(x, end=' ')
# #혹은 아래 답변
# print()
# for x in range(0,a+1):
#     if x%3==0:
#         print(x)

#실습 - 숫자 두개와 기호를 입력 받아 계산기
# a=int(input('첫번째 숫자는'))
# b=input('기호를입력해주세요')
# c=int(input('두번째 숫자는'))
# while True:
#     if b=='+':
#         print('%d + %d = %d'%(a,c,a+c))
#         break
#
#     elif b=='-':
#         print('%d - %d = %d'%(a,c,a-c))
#선생님 답변

# while True:
#     a = int(input('첫번째 숫자는'))
#     b = input('기호를입력해주세요')
#     c = int(input('두번째 숫자는'))
#     if b == '+':
#         print(a+c)
#     elif b == '-':
#         print(a-c)
#     elif b=='*':
#         print(a*c)
#     elif b=='/':
#         print(a/c)
#     else:
#         print("잘못된 기호")
#     if input('종료?')=='y':
#         break


# while True:
#     a = (input('첫번째 숫자는'))
#     if a=='q' : break
#     a=int(a)
#
#     while True:
#         b = input('기호를입력해주세요')
#         if b in ['+','-','*','/']:
#             break
#
#
#     c = int(input('두번째 숫자는'))
#     if b == '+':
#         print(a+c)
#     elif b == '-':
#         print(a-c)
#     elif b=='*':
#         print(a*c)
#     elif b=='/':
#         print(a/c)
#     else:
#         print("잘못된 기호")

#실습5)
# dicA={1:94,2:87,3:91, 4:75, 5:92}
# print(dicA.keys())
# print(dicA.values())
# print(dicA.items())
#
# for no,score in dicA.items():
#     if score>=90:
#         print(no,'번',score,'점')

#실습 6)
# 사원의 판매수량 입력
# 히스토그램 그리기
data = ['홍길동','이순신','김순희','이철수']
qty={}
for name in data:
    qty[name] = int(input(name+'?'))

print(qty)

for name,qty in qty.items():
    print(name,'*'*qty)