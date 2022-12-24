'''
    턱걸이 평균 측정 프로그램을 만들어 보시오.
    먼저, 턱걸이 횟수를 저장할 빈 리스트를 만드시오.
    그리고 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장하시오.
    리스트에 저장된 데이터의 평균을 구해 출력하시오.

    예)
        1일차 턱걸이 횟수 >>
        2일차 턱걸이 횟수 >>
        3일차 턱걸이 횟수 >>
        4일차 턱걸이 횟수 >>
        5일차 턱걸이 횟수 >>
        6일차 턱걸이 횟수 >>
        7일차 턱걸이 횟수 >>

        평균 >> 22
'''
count = []
count.append(int(input("1일차 턱걸이 횟수 >> ")))
count.append(int(input("2일차 턱걸이 횟수 >> ")))
count.append(int(input("3일차 턱걸이 횟수 >> ")))
count.append(int(input("4일차 턱걸이 횟수 >> ")))
count.append(int(input("5일차 턱걸이 횟수 >> ")))
count.append(int(input("6일차 턱걸이 횟수 >> ")))
count.append(int(input("7일차 턱걸이 횟수 >> ")))
print(count)
sum(count)
print(sum(count))
avg = sum(count) / len(count)
print("평균 >> " ,avg)