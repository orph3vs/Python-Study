# 파이썬 코딩 대회
# 참석률을 높이기 위해 댓글 이벤트 진행
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 줌
# 추첨 프로그램 제작

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 활용

from random import *
#comment_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
comment_list = list(range(1,21)) # type이 range가 됨 > list 함수 사용을 위해 list로 변환
correct_list = {}

shuffle(comment_list)
#print(comment_list)
correct_list = sample(comment_list, 4)
print("치킨 : " + str(correct_list[0]) + " 커피 : " + ' '.join(str(x) for x in correct_list[1:]))
print("치킨 : {0}".format(correct_list[0]) + " 커피 : {0}".format(correct_list[1:]))