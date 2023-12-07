# 입출력
import sys
# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재밌을까요?")
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러로 처리

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 대기 순번표
# 001, 002, 003 ...
# for number in range(1,21):
#     # print("대기번호 : " + str(number))
#     print("대기번호 : " + str(number).zfill(3))

# answer = input("아무 값이나 입력하세요. : ")
# print("입력하신 값은 " + answer + "입니다.")

# 다양한 출력 포멧
'''
# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호 붙이기
print("{0:+,}".format(-1000000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호 붙이기, 자릿수 확보, 빈자리 ^ 채움
print("{0:^<+30,}".format(-1000000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 특정 자릿수 
print("{0:.2f}".format(5/3))
'''
