# 문자열
'''
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)

# 슬라이싱
jumin = '990120-1234567'
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 ~ 2 직전까지(0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
print("뒤 7자리(뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째 부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)
print(python.find("Java"))
#print(python.index("Java"))
print(python.count("n"))


# 문자열 포멧
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c 로 시작해요." % 'A')
# %s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아합니다." % ("파란", "빨간"))

print("나는 {}살입니다.".format(20))
print("나는 {1}색과 {0}색을 좋아합니다.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
print("백문이 불여일견 \n백견이 불여일타") # \n 줄바꿈
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.") #\" 
'''
# \\ : 문자 내에서 \
print("C:\\Users\\orph3vs")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple 덮어써짐

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple")

# \t : tab
print("Red\tApple")