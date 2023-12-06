# 리스트
'''
# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호가 몇 번째 칸인지?
# print(subway.index("조세호"))

# # 하하 가 다음 정류장에서 탐
# subway.append("하하")
# print(subway)

# # 정형돈 유재석 / 조세호 사이에 태움
# subway.insert(1, "정형돈")
# print(subway)

# # 뒤에서 부터 꺼냄
# print(subway.pop())
# print(subway)

# # 카운트.
# print(subway.count("유재석"))

# 정렬
num_list = [5,2,4,3,1]
num_list.sort() 
print(num_list)
# 역순
num_list.reverse()
print(num_list)
# 리스트 삭제(안에 값을 삭제)
# num_list.clear()
# print(num_list)
# 리스트에는 여러 타입의 값이 들어갈수 있음
mix_list = ["조세호", 20, True]
print(mix_list)
# 리스트 확장
num_list.extend(mix_list)
print(num_list)
'''

# 사전dict (key, value)
'''
cabinet = {3:"john", 100:"mike"}
print(cabinet[3], cabinet[100])
print(cabinet.get(3))
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) # T
print(5 in cabinet) # F

cabinet = {"A-3":"john", "B-100":"mike"}
print(cabinet)
cabinet["A-3"] = "tony" # 교체
cabinet["C-20"] = "jimmy" # 추가
print(cabinet)
del cabinet["A-3"] # 삭제
print(cabinet)
print(cabinet.keys()) # 키 확인
print(cabinet.values()) # 값 확인
print(cabinet.items()) # 키+값 확인

cabinet.clear()
print(cabinet)
'''
# 튜플
'''
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
#menu.add("생선까스") # 튜플엔 add 못씀

(name, age, hobby) = ("john", 20, "코딩")
print(name, age, hobby)
'''

# 집합(set) 중복 안됨, 순서 없음
'''
my_set = {1,2,3,3,3}
print(my_set)

java_dev = {"john", "tony", "mike"}
python_dev = set(["john", "jimmy"])

# 교집합 (자바, 파이썬 모두, and)
print(java_dev & python_dev)
print(java_dev.intersection(python_dev))

# 합집합 (자바, 파이썬 둘중의 하나, or)
print(java_dev | python_dev)
print(java_dev.union(python_dev))

# 차집합 (자바는 할수 있지만 파이썬은 모르는 .)
print(java_dev - python_dev)
print(java_dev.difference(python_dev))

# 교육 후 파이썬 개발자가 늘어남
python_dev.add("tony")
print(python_dev)

# 자바를 까먹음
java_dev.remove("tony")
print(java_dev)
'''
# 자료구조의 변형
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
