# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") # write
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
# score_file = open("score.txt", "a", encoding="utf8")  # append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()
# score_file = open("score.txt", "r", encoding="utf8")   # read
# print(score_file.read())
# score_file.close()
# score_file = open("score.txt", "r", encoding="utf8")   # read
# print(score_file.readline(), end="") # 줄 별로 읽기, 커서는 다음 줄로
# print(score_file.readline(), end="")
# score_file.close()
# score_file = open("score.txt", "r", encoding="utf8")   # read
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()
# score_file = open("score.txt", "r", encoding="utf8")   # read
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

# pickle
import pickle
# profile_file = open("profile.pickle", "wb") # b 필수, 인코딩 불필요  첫인자 : 파일명
# profile = {"이름":"john", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file 에 저장
# profile_file.close()
# profile_file = open("profile.pickle", "rb") # b 필수, 인코딩 불필요
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with
# with open("profile.pickle", "rb") as profile_file: # close가 필요가 없다.
#     print(pickle.load(profile_file))
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())