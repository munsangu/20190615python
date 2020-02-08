Max_Weight = 600
object1 = float(input("첫 번째 물건의 무게를 입력하세요 :"))
object2 = float(input("두 번째 물건의 무게를 입력하세요 :"))

Current_Weight = float(Max_Weight - (object1 + object2))
print("현재 엘리베이터의 허용 무게는", Current_Weight , "Kg 입니다.")
