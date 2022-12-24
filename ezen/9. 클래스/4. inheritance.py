'''
    1. 상속: 클래스들에 중복된 코드를 제거하고 유지보수를 편하게 하기 위해서 사용.

                            몬스터

           땅 몬스터        물 몬스터        공중 몬스터

    2. 부모 클래스 정의
        - 속성
            - 이름, 체력, 공격력
        - 함수
            - 이동하기(move)
'''
# 부모 클래스
class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}의 체력: {health}  공격력: {attack}")

    def move(self):
        print(f"{self.name}(이)가 이동했습니다.")

# 자식 클래스
class EarthMonster(Monster):
    def move(self):             # 메서드 오버라이딩
        print(f"[{self.name}](이)가 뛰어갑니다.")

class WaterMonster(Monster):
    def move(self):             
        print(f"[{self.name}](이)가 헤엄쳐갑니다.")

class AirMonster(Monster):
    def move(self):
        print(f"[{self.name}](이)가 날아갑니다.")

Wolf = EarthMonster("엄청 큰 늑대", 800, 150)
Shark = WaterMonster("배고픈 상어", 1000, 200)
Dragon = AirMonster("빠른 드래곤", 999, 999)

Wolf.move()
Shark.move()
Dragon.move()