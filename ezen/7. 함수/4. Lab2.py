'''
    로또 예상번호 추출 프로그램을 구현하려고 합니다.
    다음 조건에 따라 프로그램을 완성해보시오.
        1) 로또 번호를 6개를 추출한다
        2) 로또 번호는 1~45까지의 랜덤한 번호다
        3) 6개의 숫자는 모두 달라야 한다
        4) get_random_number() 함수를 사용해서 구현한다.

        출력 예) 1  8  23  43  24  17

        - 리스트, 반복문, 조건문
'''
import random
def get_random_number():
    number = random.randint(1, 45)
    return number

# 로또 번호 리스트
lotto_num = []
# 현재 뽑은 숫자 개수
i = 0

while True:
    if i > 5:
        break
    number = get_random_number()

    if number not in lotto_num:
        lotto_num.append(number)
        i += 1

lotto_num.sort()
for n in lotto_num:
    print(n, end=" ")