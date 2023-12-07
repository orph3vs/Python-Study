# 함수
'''
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money: # 잔액이 출금보다 많으면 
        print("출금 완료. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금 불가. 잔액은 {0}원입니다.".format(balance))
        return balance
def withdraw_night(balance, money):
    commission = 100 # 수수료
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))
'''
# 기본값
'''
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
            .format(name, age, main_lang))
profile("john", 20, "python")
profile("tony", 25, "java")

# 같은 학교 같은 학년 같은 반 같은 수업.
def profile(name, age=17, main_lang="python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
            .format(name, age, main_lang))
    
profile("john")
profile("tony")

# 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="john", main_lang="python", age=20)
profile(name="tony", age=25, main_lang="java")

# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") # 이어 출력. 줄바꿈X
#     print(lang1, lang2, lang3, lang4, lang5)
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") # 이어 출력. 줄바꿈X
    for lang in language:
        print(lang, end=" ")
    print()

profile("john", 20, "Python", "java", "C", "C++", "C#", "javascript") 
profile("tony", 25, "Kotlin", "Swift")
'''
# 지역변수, 전역변수
gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명 경계근무
gun = checkpoint_ret(gun, 2) # 인자로 전달할 경우 전역으로 인식?
print("남은 총 : ", gun)