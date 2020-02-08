class Fruit:
    def __init__(self,gram,price):
        self.gram = gram
        self.price = price
    def printInfo(self):
        print("무게 : %d g, 가격: %d 원"%(self.gram,self.price))

class WatterMelon(Fruit):
    def printInfo(self): # 부모의 메소드 기능을 덮어씌우는 것 -> 오버라이딩
        print("무게 : %.2f Kg, 가격: %d 원"%(self.gram * 0.001,self.price))

banana = Fruit(500,3000)
banana.printInfo()
wattermelon = WatterMelon(1600,5000)
wattermelon.printInfo()
