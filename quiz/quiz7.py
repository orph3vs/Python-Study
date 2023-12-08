# 매주 1회 작성해야 하는 보고서가 있다.
# - X 주차 주간보고 - 
# 부서 : 
# 이름 :
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt' ... 와 같이 만듬.

# open, pickle, with
for number in range(1,51):
    with open("{0}주차.txt".format(number), "w", encoding="utf8") as file:
    #with open(str(number) + "주차.txt", "w", encoding="utf") as file:
        file.write("- {0} 주차 주간보고 -".format(number))
        file.write("\n부서 : ")
        file.write("\n이름 : ")
        file.write("\n업무 요약 : ")

print("파일 작성 완료!!!")