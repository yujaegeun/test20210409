#딕셔너리
#순서가 없다.
# data={'a':10,'b':20,'c':30,'d':40}
# print(data['a'])

#
# data={'홍길동':20,'이순신':45}
# print(data['홍길동'],'살')
#
#
# data={'홍길동':[20,165.5],'이순신':45}
# print(data['홍길동'][1])
#
# data={'홍길동':{'나이':20,'키':165.5},'이순신':{'나이':45,'키':178.8}}
#
# print(data['홍길동']['키'])
# print(data['이순신']['나이'])
#
# data={1:['홍길동',20,165.5], 2:['이순신',45,178.9]}
# print(data[1])
# print(data[2][0])
#
#
# #딕셔너리에 데이터 추가
# data={}
# data['홍길동']=20
# data['이순신']=40
# print(data)



#실습) 컴퓨터 언어를 입력받아 딕션너리에 저장
#{'backend' : "java",'frontend':html'}
#내 답안지
# lang={}
#
# back=input('backend언어는?')
# lang['backend']=['java']
# print(lang['backend'])
#
# frontend=input('frontend언어는?')
# lang['frontend']=['html']
# print(lang['frontend'])
#
# #선생님 답안지
# lang={}
# back = input('backend언어는?')
# lang['backend'] = back
# front = input('frontend언어는?')
# lang['frontend'] = front
# print(lang)

#
data={1:'고질라',2:'귀멸의칼날',3:'더박스'}
print((data.keys()))
print(list(data.keys())) # 키 값은 []로 못 불러옴
print(data.values())
print(list(data.values()))
print(list(data.values())[2])
