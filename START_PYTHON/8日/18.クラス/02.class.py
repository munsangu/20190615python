# 내가 만드는 자료형
# 자바는 모든 기능이 클래스로 구현되어 있음 => 문법이 長
# 상속, 오버라이딩
class Adder: #계산기 클래스 선언
    # 클래스 내부의 함수를 메소드
    # 클래스 내부의 변수를 멤버변수(필드)
    # 문자열 내장함수
    def __init__(self): # 생성자 : 클래스로 객체를 만들때 바로 호출되는 함수
        self.result = 0 # 내 객체 내부에 result 필드를 만들어 줌
    def adder(self, num):
        self.result += num
        return self.result

cal1 = Adder() #Adder클래스를 이용하여 cal1객체 생성
cal2 = Adder() #Adder클래스를 이용하여 cal2객체 생성
print(cal1.adder(2))
print(cal1.adder(4))
print(cal2.adder(5))
print(cal2.adder(6))
