# firstname : 성
# lastname : 이름

# firstname = input("성 입력: ")
# lastname = input("이름 입력: ")
# change_name(firstname,lastname) #jinwoo song

def change_name(a,b):
    print(b + " " + a)

firstname, lastname = input("성 입력: "), input("이름 입력:")
change_name(firstname,lastname)


def  change_name(a):
    x,y = a.split()
    print(y + " " + x)

name = input("성, 이름 입력:")
change_name(name)
