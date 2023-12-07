# practice memo
'''
my_set = {1,2,3,3,3}
print(my_set)

my_list = [1,'a', 3]
print(type(my_list))

my_tuple = (1,'b',4)
print(type(my_tuple))

a = [1, 2, 3, 4, 5] 
print(' '.join(str(x) for x in a))

python = "Python is Amazing"
print(python.index('n',3,7))
print(python.find('n',6,9))

for x in range(1,10):
    print(x)

from random import *
for i in range(1,11):
    print(randrange(9,10))
    
print(((175/100)*2)*22)
print(pow(1.75,2)*22)
print(round(67.375,2))
'''
import re
# a, b = input("입력 두 개 : ").split(',')
# print(a, b)
# a = int(a)
#print(type(a), type(b))
text = "a, b,c d"
result = re.split(r'[,\s]+', text)
print(result)