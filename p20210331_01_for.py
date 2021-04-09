#반복문 : for

#예시
# for x in [1,2,3,4,'f']:
#     print('python',x)

# data=['박영준','김영빈','송석화']
# for x in data:
#     print(x)
#
# for x in [0,1,2]:
#     print(data[x])

#실습)0~9출력

data=[0,1,2,3,4,5,6,7,8,9]
for x in data:
    print(x)

#정수를 생성
#range(start 값,stop 값,step 값)
# print(list(range(10,101,1)))
# print(list(range(101))) #stop
# print(list(range(10,20))) #statr,stop

# for x in range(0,101,2):
#     print(x)

#합계를 구하기
# s=0 # 합계를 저장할 변수
# for x in range(1,10001):
#     s += x #s = s+x 같은것
# print(s)

#실습) 입력숫자를 받아 1부b터 그 수까지 더하기
# a= int(input('숫자를입력하세요'))
#
# b=0
# for a in range(1,a+1):
#     b=b+a
# print(b)

#실습) 1부터 100까지 합이 2000이 넘는때에 수를 출력
s=0
for x in range(1,101):
    s += x
    if s>2000:
        break #반복문을 종료할 때

print('x=',x,'s=',s)

#실습 바보라는 글자가 발견되면 강퇴


# data = ['안녕','반가워','방가','2','오늘만나']
# bad = ['바보','멍청이']
# for x in data:
#     print(x)
#     if x in bad:
#         print('강퇴')
#         break
# else: #FOR문이 정상 수행 했다면(break문을 실행하지 않았을때)
#     print('바른말사용')

#continue : 계속 진행
# data=[3,4,6,8,7,10]
# for x in data:
#     if x%2==1:continue
#     print(x)

#실습) 60점이 넘으면 합격하는 프로그램 작성

#내 답변
# a=int(input("첫과목"))
# b=int(input("두번째과목"))
# c=(a+b)/2
# if c>60:
#         print('합격')
# else:
#     print('불합격')

#선생님 답변
# data=input('점수는').split()
# print(data)
# data = map(int,data)
# for x in data:
#     print(x)
#     if x<60:
#         print("불합격")
#         break
# else:
#     print('합격')

# 합계가 300이상 일 경우 합격
# s=0
# data=[65,45,95,55,70]
# for x in data:
#     s+=x
#     if s>=300:
#         print("합격")
#         break
# else:
#     print("불합격")
# #set: 중복 데이터 허용 불가
# asia={'한국','중국','일본'}
# asia.add('베트남')
# asia.add('중국')
# asia.remove('일본')
# asia.update({'한국','홍콩','태국'})
# print(asia)