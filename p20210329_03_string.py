#문자열다루기
txt = 'python is easy!'
print(txt)
print(txt[0])
print(txt[-1]) # 마지막인덱스
print(txt[7:9]) #start index : stop index
print(txt[0:2]) # 혹은 [:2]
print(txt[10:14]) # 혹은 [10:-1],[-5:-1]
print(txt[-5:]) # 0은 생략 가능

# 실습

txt = 'my house'
print(txt[3:8])

txt = '012345678901234567890123456'
print(txt[0:10])
print(txt[10:20])
print(txt[-6:]) # 혹은 [20:]


