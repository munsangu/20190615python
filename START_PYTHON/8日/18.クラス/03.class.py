class Waffle: #와플 틀
    taste = "무맛" # self.을 안붙여도 변수 선언 가능(메소드 외부에서만 가능)
    def __init__(self, taste):#self : 내 객체, self외에 매개변수가 추가되면
        #객체 생성시에 넣어줘야한다
        self.taste = taste # taste가 매개변수인지 내 객체의 taste인지 구분못함
        # 메소드 내부에서는 매개변수가 더 우선시 됨. => self는 내 것이라는 뜻
    def show_taste(self):
        return self.taste

waffle1 = Waffle("플레인")
print(waffle1.show_taste())
waffle2 = Waffle("딸기")
print(waffle2.show_taste())
