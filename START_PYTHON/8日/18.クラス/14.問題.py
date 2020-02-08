class Animal:
    def __init__(self, weight, sound):
        self.weight = weight
        self.sound = sound
    def sleep(self):
        print("코 잔다")
    def speak(self):
        print(self.sound)
    def eat(self):
        print("먹는다")
    def show(self):
        print("동물 : %.2fkg"%self.weight)
class Cat(Animal):
    def eat(self):
        print("생선을 먹는다")
    def show(self):
        print("고양이 : %.2fkg"%self.weight)
class Dog(Animal):
    def eat(self):
        print("개껌을 먹는다")
    def show(self):
        print("개 : %.2fkg"%self.weight)

ani= Animal(0,"멍멍냥냥")
ani.sleep()
ani.speak()
ani.eat()
ani.show()

cat = Cat(5.3, "냥냥")
cat.sleep()
cat.speak()
cat.eat()
cat.show()

dog = Dog(6.5, "멍멍")
dog.sleep()
dog.speak()
dog.eat()
dog.show()
