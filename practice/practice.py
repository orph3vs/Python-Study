'''
# 숫자
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(3*3+1)
print(3*(3+1))

#문자열
print('풍선')
print("나비")
print('ㅋ'*9)

#참/거짓
print(5>10)
print(10>5)
print(True)
print(not True)
print(not False)
print(not(5>10))
'''

# 애완동물을 소개해 주세요~
animal = "고양이"
name = "나비"
age = 2
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + " 이름은 " + name + "예요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, " + hobby +"을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby,"을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))