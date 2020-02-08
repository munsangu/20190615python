# money = int(input("밥 뭐 먹을까? 얼마있어? :"))
# if money >= 50000:
#     print("소고기 먹으러 가자")
# else:
#     if money >= 30000:
#         print("돼지고기 먹자")
#     else:
#         if money >= 10000:
#             print("짬뽕 먹자")
#         else:
#             print("편의점가서 먹어야지")

# if ~ else => if ~ elif ~ else가 한 짝
# 안에 문장이 실행되면 밖으로 빠져나감 => 다음 문장 실행
money = int(input("밥 뭐 먹을까? 얼마있어? :"))
if money >= 50000:
    print("소고기 먹으러 가자")
elif money >= 30000:
    print("돼지고기 먹자")
elif money >= 10000:
    print("짬뽕 먹자")
else:
    print("편의점가서 먹어야지")
