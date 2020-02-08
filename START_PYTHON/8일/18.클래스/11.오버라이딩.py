class Bank:
    money = 0
    def __init__(self, name, num):
        self.name = name #은행이름
        self.num = num #은행계좌
    def Deposit(self, money):
        if money > 0:
            self.money += money
            print("%s은행 %s계좌로 %s원 입금"%(self.name,self.num,self.money))
        else:
            print("잘못된 입력입니다.")
# 메소드 오버라이딩: 상속받는 클래스(부모클래스)의 메소드를 같은 이름 다른 기능으로 덮어씌움
class BusanBank(Bank):
    def __init__(self, num):
        self.num = num #은행계좌
    def Deposit(self, money):
        if money > 0:
            self.money += money
            print("부산은행  %s계좌로 %s원 입금"%(self.num,self.money))
        else:
            print("잘못된 입력입니다.")

bank = Bank("부산","1122014901801")
bank.Deposit(5000)
bank.Deposit(-5000)
