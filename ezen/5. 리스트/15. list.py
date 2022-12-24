'''
    * 리스트 자료형
        - 리스트명 = [데이터, 데이터, 데이터, ...]
'''

# 데이터가 없는 리스트
empty = []

# 데이터가 있는 리스트
animal = ["사자", "호랑이", "독수리", "곰"]

# 데이터 조작하기
# 인덱스는 0부터 시작함
print(animal[2])
print(animal[-1])

# 데이터 추가하기
animal.append("원숭이")
print(animal)

# 데이터 할당하기
animal[1] = "토끼"
print(animal)

# 데이터 삭제하기
del animal[0]
print(animal)

# 데이터 슬라이싱
print(animal[1:3])
print(animal[:])
print(animal[:2])
print(animal[2:])

# 리스트 길이
print(len(animal))

# 리스트 정렬
animal.sort()
print(animal)