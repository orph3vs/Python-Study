# 표준 체중을 구하는 프로그램 작성
# *표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
# *함수명 : std_weight
# *전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# ex) 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        return pow((height/100),2)*22       
    elif gender == "여자":
        return pow((height/100),2)*21
    else:
        print("incorrect input.")

h, g = input("키와 성별을 입력하시오. ex) 175 남자 : ").split()

print("키 {0} {1}의 표준 체중은 {2} kg입니다.".format(h, g, round(std_weight(int(h), g),2)))