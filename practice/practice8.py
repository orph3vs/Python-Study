# Class
'''
# 마린 : 공격 유닛, 총을 쏨
name = "마린" # 이름
hp = 40 # 체력
damage = 5 # 공격력
print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏨. 일반 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
'''
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # 생성자 : 만들어질때 자동으로 호출됨
        self.name = name  # 멤버 변수
        self.hp = hp
        self.speed = speed
        # self.damage = damage
        # print("{0} 유닛이 생성되었습니다.".format(self.name))  
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):  # 상속
    def __init__(self, name, hp, speed, damage): # 생성자 : 만들어질때 자동으로 호출됨
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location): # method , 클래스 내의 함수
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 공격 불가, 수송선
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))  

class FlyableAttackUnit(AttackUnit, Flyable):  # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0       
        Flyable.__init__(self, flying_speed)   

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


        
'''
# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
       # pass  # 아무것도 안하고 넘어감
       super().__init__(name, hp, 0) # (), self 안씀
       self.location = location

# 서플라이 디폿 : 건물, 1 = 8 유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    pass

game_start()
game_over()


# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 고성능유닛
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")    
battlecruiser.move("9시")


# 발키리 : 공중 공격 유닛, 한번에 14발 미사일
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 객체 생성 init에 설정한 인자 수를 맞춰야 함
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 뺏음
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True     # 클래스 외부에서 추가 변수를 만들어 쓸 수 있다. wraith1 에는 없음. 기존 객체에는 없음.

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
   
# 메딕 : 회복 유닛
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
 '''