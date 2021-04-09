#튜플

#data=(10,20,30,40,50)
# data=10,20,30,40,50 # 소괄호를 사용 안해도 괜찮다
# print(data[0])
# # data[1] = 200 / 변경이 불 가능하다

#두 수를 바꾸기 (순서)

# a=10;b=20
#
# temp=a
# a=b
# b=temp
#
# print(a,b)


# 패킹과 언패킹

a=10;b=20;
b,a=a,b
print(a,b)

a= 1; b=2; c=3
a,b,c=c,a,b
print(a,b,c)
