mart = {"다이제":800, "메로나":500, "코카콜라":700, "츄파츕스":200}

print("\n===key 리스트 만들기===")
mart_menu = list(mart.keys()) # key만 들고와서 list로 만들어줌
print(mart_menu)
print(mart_menu[2])

print("\n===value 리스트 만들기===")
mart_price = list(mart.values())
print(mart_price)
print(mart_price[2])

print("\n===key로 value 들고오기===")
print(mart.get("다이제"))
print(mart["다이제"])

print("\n===☆☆☆☆☆ 해당 key가 있는지 찾아보기===")
# in : ~ 안에 있다
# not in : ~ 안에 없다
# 컴퓨터에게 물어봄 => True, False 로 답을 알려줌
# 딕셔너리 자료형은 Key에서 찾아봄
print("다이제" in mart)
print("플레이스테이션4" in mart)

mart_menu = ["다이제", "메로나", "츄파츕스"]
print("다이제"in mart)
print("플레이스테이션4"in mart)

mart_menu = "다이제", "메로나", "츄파츕스"
print("다이제" in mart_menu)

print("\n=== key로 value를 모두 지우기===")
# del mart => mart 변수가 지워짐
mart.clear()
print(mart)
