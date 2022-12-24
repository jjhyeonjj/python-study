'''
    구구단 출력 프로그램을 만들어 보시오.
    사용자로부터 출력할 단을 입력 받고, 해당 구구단을 출력하는 프로그램입니다.

    몇 단을 출력할까요? >>>

    5 * 1 = 5
    5 * 2 = 10
    ...
    5 * 9 = 45
'''
dan = int(input("몇 단을 출력할까요? >> "))
i = 1
while i<10:
    print(dan, 'x' , i, '=', dan * i)
    i += 1

print()

dan2 = int(input("몇 단을 출력할까요? >>"))
j = 1
for j in range(1, 10):
    print(dan2, 'x' , j, '=', dan2 * j)