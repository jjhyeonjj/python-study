'''
    세 개의 정수를 인자로 받아,
    합계와 평균을 출력해주는 함수를 만드시오.

    예시) 합계:    평균:
'''
# def print_sum_avg(a, b, c):
#     print("합계:", a + b + c, "   평균:", (a + b + c) / 3)
#
# x = int(input("첫 번째 수 >> "))
# y = int(input("두 번째 수 >> "))
# z = int(input("세 번째 수 >> "))
#
# print_sum_avg(x,y,z)

# 설명문(docstring)    """
# 문자열 포매팅(f"")
def print_sum_avg(a, b, c):
    """
    세 개의 숫자를 받아 합계와 평균을 출력하는 함수
    :param a:
    :param b:
    :param c:
    :return:
    """
    sum = a + b + c
    avg = sum / 3
    print(f"합계: {sum} 평균: {avg}")

print_sum_avg(12, 14, 16)
print_sum_avg(43, 34, 23)