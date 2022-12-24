# 비만도 계산기를 만들어 보시오.
# (체중)/(신장(m))^2
'''
예시)
    BMI 계산기 입니다.
    신장: (입력)
    체중: (입력)
    BMI: (출력)
'''

print("BMI 계산기입니다.")
t = float(input("신장(m): "))
w= float(input("체중(kg): "))
BMI = float(w/(t*t))
print("BMI:", BMI)