# 사용자로부터 데이터를 입력 받는 함수 (input())
# x = input()
#   1) 할당연산자(=) 오른쪽부터 실행
#   2) input() 함수 실행 시, 입력을 기다림
#   3) 사용자가 데이터를 입력하고 엔터를 침
#   4) input() 함수 자리에 데이터가 들어감

# x = input("입력하세요>>>")
#   1) 할당연산자(=) 오른쪽부터 실행
#   2) input() 함수 실행 시, 입력을 기다림
#   3) 사용자가 데이터를 입력하고 엔터를 침
#   4) input() 함수 자리에 데이터가 들어감

# 사용자로부터 두 개의 숫자를 입력받고, 더한 결과를 출력하시오
x = input("첫번째 숫자 입력 >>")
y = input("두번째 숫자 입력 >>")

# 자료형 확인하기: type(x)
# str = string = 문자열
# print(type(x))
# print(type(y))
# result = x + y

# 숫자형으로 변환: int(데이터)
result = int(x) + int(y)
print(result)
