# 사용자로부터 태어난 연도를 입력 받으면,
# 현재 나이를 출력하시오.
# ex) 태어난 연도를 입력하세요 >>> 2000
#     현재 나이는 22세입니다.

year = input("태어난 연도 입력 >> ")
age = 2022 - int(year) + 1
print("현재나이는" , age, "세 입니다.")

