mart = {"다이제":1000, "메로나":500, "코카콜라": 700, "츄파츕스":500}
mart_menu = tuple(mart.keys())
print(mart_menu)

price = sum(mart.values())
print(price)

mart[input("과자 :")] = int(input("가격:"))
print(mart)

# 언패킹 : 오른쪽 데이터를 차례대로 왼쪽에 대입
mart_key, mart_price = input("과자 :"), int(input("가격 :"))
mart[mart_key] = mart_price
print(mart)
