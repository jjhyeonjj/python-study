'''
    상속의 업그레이드
        - 클래스 변수(인스턴스들이 모두 공유하는 변수)

        - 예
            드래곤 클래스에 인스턴스 속성을 추가하기
            부모 클래스에 클래스 변수 추가하기
'''
import random


# 부모 클래스
class Monster:
    max_num = 1000      # 클래스 변수
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}의 체력: {health}  공격력: {attack}")
        Monster.max_num -= 1

    def move(self):
        print(f"{self.name}(이)가 지상 이동합니다.")

# 자식 클래스
class EarthMonster(Monster):
    def move(self):             # 메서드 오버라이딩
        print(f"[{self.name}](이)가 뛰어갑니다.")

class WaterMonster(Monster):
    def move(self):
        print(f"[{self.name}](이)가 헤엄쳐갑니다.")

class AirMonster(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("불뿜기", "꼬리치기", "날개치기")


    def move(self):
        print(f"[{self.name}](이)가 날아갑니다.")

    def skill(self):
        print(f"[{self.name}](이)가 [{self.skills[random.randint(0,2)]}]스킬을 사용합니다.")

Wolf = EarthMonster("늑대", 1500, 200)
Wolf.move()
print(Wolf.max_num)

Shark = WaterMonster("상어", 3000, 400)
Shark.move()
print(Shark.max_num)

Dragon = AirMonster("드래곤", 8000, 950)
Dragon.move()
Dragon.skill()
print(Dragon.max_num)
