class Unit:
    def __init__(self,name,life,dmg):
        self.name = name
        self.life = life
        self.dmg = dmg
    def attack(self,Unit): #Unit = zergling
        Unit.life -= self.dmg
    def show(self):
        print("[%s] : LIFE : %d"%(self.name,self.life))

marine = Unit("마린", 40, 5)
zergling = Unit("저글링", 35, 6)

marine.attack(zergling)
marine.attack(zergling)
zergling.show()

zergling.attack(marine)
zergling.attack(marine)
marine.show()
