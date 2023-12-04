'''
print(2**3) #square
print(5%3) # 나머지
print(5//3) # 몫
print(10>=3)
print(3==3) # Equal
print(1!=3) # not Equal
print(not (1!=3))
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 2))
print((3 > 0) | (3 < 2))
print(5>4>3)
print(5>4>7)
number = 10
number += 10
print(number) # 20
number*=2
print(number) # 40
number%=3
print(number) # 1

print(abs(-5)) # 5
print(pow(4,2)) # 4^2
print(max(5,12)) # 큰값
print(min(5,12)) # 작은값
print(round(3.14)) # 반올림
print(round(4.99))

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근
'''

from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의값 생성
# print(random()*10) # 0.0 ~ 10.0 미만의 임의값 생성
# print(int(random()*10))
# print(int(random()*10+1)) # 1 ~ 10 이하
print(int((random()*45)+1)) # 1 ~ 45
print(randrange(1,46)) # 1 ~ 45 
print(randint(1,45)) # 1 ~ 45 1과 45 포함
