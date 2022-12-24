'''
    1. 함수의 기본 형태
    def 함수 이름():
        명령 블록

    함수 호출하기
        함수 이름()

    2. 함수의 매개변수가 있는 형태
        def 함수 이름(매개변수1, 매개변수2):
            명령 블록

        함수 호출하기
            함수 이름(인자1, 인자2)

    3. 함수의 반환값이 있는 형태
        def 함수 이름():
            명령 블록
            return 반환값

        함수 호출하기
            함수 이름()

    4. 함수의 매개변수와 반환값이 있는 형태
        def 함수 이름(매개변수1, 매개변수2):
            명령 블록
            return 반환값

        함수 호출하기
            함수 이름(인자1, 인자2)
'''
def printMessage(name, date):
    print("안녕하세요. ", name, "님", sep="")
    print("현재 2022년도 쿠폰 사용 남은 기간이", date, "일 남았습니다.")

printMessage("이순신", 30)
printMessage("신사임당", 25)
printMessage("이방원", 19)
printMessage("이성계", 45)
