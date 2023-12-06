# 택시 기사임
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해짐
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭

# 출력문 예제
# [O] 1번째 손님 (소요시간 : 15분)
# [X] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [X] 50번째 손님 (소요시간 : 16분)

from random import *
counter = 0

for customer in range(1,51):
    time = randrange(5,51)
    if 15 >= time >= 5:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        counter += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))

print("총 탑승객 수 : {0} 명".format(counter))