a= int(input("태어난 해: "))
b= int(input("태어난 월: "))
c= int(input("태어난 일: "))

if (a-b+c) % 10 == 0:
    print("대박!")
else:
    print("그럭저럭")
