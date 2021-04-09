#내장함수
#sum
# data=[5,8,4,6]
# sum(data)
# print(sum(data))

#사용자 함수 sum정의
# 매개변수 : 리스트,반환값:합계
# def mysum(data):
#     s=0
#     for x in data:
#         s +=x
#
#     #print(s)
#     return s
#
#
# data=[2,3,4,5,6]
# r = mysum(data)
# print('리턴값',r)


#max 함수 min 함수
# data=[5,18,4,6]
# m=max(data)
# n=min(data)
# print(m,n)

#data=[5,18,4,6]



#max 함수 정의
# def mymax(data):
#     mx = data[0]
#     for x in data:
#         if x>mx:
#             mx=x
#     return mx
#
# data = [5, 18, 4, 6]
# print(mymax(data))

#min 함수 정의
# def mymin(data):
#     mn = data[0]
#     for x in data:
#         if x<mn:
#             mn=x
#     return mn
# data=[50,80,40,70,10]
# print(mymin(data))
# data=[403,751,152,101,100]
# print(mymin(data))


#ord()함수
#한글은 유니코드체계
# print(ord('A'), len('A'),'A'.encode(),len('A'.encode()))
# print(ord('가'), len('가'),'가'.encode(),len('가'.encode()))
#
# print(chr(44032))

#실습)두수 입력 받아서 사칙연산 함수
#매개변수 : 두 수,반환값 : 결과

# def add(a,b):
#     return a + b
# def sub(a,b):
#     return a - b
#
# def cal(a,b):
#     return a+b,a-b
#
#
# print(add(10,50))
# print(sub(10,50))
# print(cal(10,50)[0])

#월급 구하기
# 년봉,시급,초과근무 시간을 매개변수로 받아
# 월급을 계산하고 반환하는 함수
# 월급 = (년봉 /12) + (시급*초과근무시간)

# 내 방법

a=int(input('연봉은?'))
b=int(input('시급은?'))
c=int(input('초과근무는?'))
def pay(a):
    return a/12
def over(b): #시급
    return b
def time(c): #초과근무
    return c

print(pay(a)+(over(b)*time(c)))
# 선생님 방법

def money(pay,over,time):
    return pay / 12 + over * time
pay = int (input('년봉은'))
over = int(input('시급은'))
time = int(input('초과근무시간'))
print(money(pay,over,time))
