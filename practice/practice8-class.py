class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자") 

#class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit):
    def __init__(self):
   #     super().__init__()  # 다중 상속시 슈퍼는 첫 클래스(인자)의 초기화값만 가져옴
        Unit.__init__(self)
        Flyable.__init__(self)
    
dropship = FlyableUnit()