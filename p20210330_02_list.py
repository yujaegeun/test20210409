#리스트 : 연속적인 메모리의 할당
#리스트 [] 대괄호에 있는 건 리스트 애들
# data=[10,20,30,40,50]
# print(data[2])
# print(data[1:3])
# print(data[2:])
# print(data[0:4]) #print(data[:-1])
#
#
# #data의 특정값을 바꿔주고 싶을 때
# data[1] = 200
# print(data)
#
#
# #data[5] = 200 # index 초과
# #추가가 안됨
# #하지만 객체를 사용하여 사용
# data.append(200)
# print(data)


data = ['홍길동',20, 165.8]
print(data[0], data[1], data[2])



data=[['홍길동',20, 165.8],['이순신',40, 170.5]]
print(data[1][0])
print(data[0][0])