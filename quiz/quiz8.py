# 주어진 코드를 활용하여 부동산 프로그램 작성

# 출력 예제
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    count = 0
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

    # # count 변수값 리턴
    # def get_count(cls):
    #     return cls.count
    
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

house_list = [house1, house2, house3]

print("총 {0}대의 매물이 있습니다.".format(len(house_list)))
for house in house_list:
    house.show_detail()

# house_list = [house1, house2, house3]
# tot_house_list = len(house_list)
# print("총 {0}대의 매물이 있습니다.".format(tot_house_list))

# for i in range(tot_house_list):
#     house_list[i].show_detail()