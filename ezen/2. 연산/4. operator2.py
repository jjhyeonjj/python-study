# 비교 연산
print(2 > 3)    # False
print(15 < 30)  # True
print(1.5 >= 0) # False
print(3 <= 3)   # True
print("주변음" == "주변옴")   # False
print("1111111111" == "1111111111") # True

# 논리 연산
print(4 < 6 and 10 >= 10)   # True and True --> True
print("적용형 주변음 허용 모드" != "적용형 주변음 허용 모드" or "나는 할 수 있다" == " 나는 할 수 있다")    # True
print(not 5 == 5) # not True --> False

# 멤버십 연산자
# in - 포함되어 있다
# not in - 포함되어 있지 않다
print("a" in "abx") # True
print("d" not in "abc") # True