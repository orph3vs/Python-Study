#월 4회 스터디, 3번은 온라인, 1번은 오프라인
#조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램 작성

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비해야 하므로 제외

# 출력문 예제
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

from random import *

online1 = randrange(4, 28)
online2 = randrange(4, 28)
online3 = randrange(4, 28)
offline = randrange(4, 28)

if(offline == (online1 or online2 or online3)):
    offline = randrange(4, 28)

print(online1, online2, online3)
print("오프라인 스터디 모임 날짜는 매월 " + str(offline) + " 일로 선정되었습니다.")