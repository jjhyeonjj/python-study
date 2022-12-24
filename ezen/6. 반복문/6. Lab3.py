'''
    순신이는 lily라는 이름의 교환학생과 친해지게 되었습니다.
    영어를 잘하지 못하는 순신은 lily에게 한국어를 가르쳐주기 위해
    한국어 연습 프로그램을 만들게 되었습니다.
        - 연습할 한국어가 담긴 리스트를 만든다
        - 리스트에서 순서대로 단어를 가져와 화면에 출력한다
        - 프로그램 사용자는 단어를 그대로 입력하고
        - 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료

        Let's Learning Korean
        사랑해
        사랑해(o)
        귀엽다
        귀엽다(o)
        고마워
        고마워(o)
        행복해
        행보캐(x)
'''
korean = ['사랑해', '귀엽다', '고마워', '행복해']
print("[Let's Learning Korean]")
for i in korean:
    print(i)
    answer = input()
    if i != answer:
        print("땡~!")
        break