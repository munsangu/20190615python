class Cookie:
    pass

a = Cookie()
b = Cookie()

print(type(a))
print(type(b))

class FourCal:
    
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second
    
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result    

    
c=FourCal(3,0)
print(c.add())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

d=SafeFourCal(4,0)
e=SafeFourCal(4,2)
print(d.div())
print(e.div())

class M:
    class_Y = 0 

a  = M()
b  = M()
print(a.class_Y)
print(b.class_Y)

M.class_Y = 5
print(a.class_Y)
print(b.class_Y)

a.class_Y=6
print(a.class_Y)
print(b.class_Y)