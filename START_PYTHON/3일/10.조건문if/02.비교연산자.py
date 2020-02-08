# num = int(input("구구단을 외자! 17 x 5: "))
# if num==17*5:
#     print("똑똑해")
# else:
#     print("세상에...")

# if ~ else 가 한 짝
# 잘못된 코드 => elif 배울때 다시 수정
money = int(input("밥 뭐 먹을까? 얼마있어? :"))
if money >= 50000:
    print("소고기 먹으러 가자")
if money >= 30000:
    print("돼지고기 먹자")
if money >= 10000:
    print("짬뽕 먹자")
else:
    print("편의점가서 먹어야지")

print("오늘도 지각이다... 대중교통을 탈까? 택시를 탈까?")
money = input("택시 탈 돈이 있나[y/n]: ")
if money == 'n':
    print("어쩔 수 없지... 대중교통 타자")
    time = input("출/퇴근 시간인가[y/n]:")
    if time == 'y':
        print("지하철타고 가자~")
    else:
        print("버스타고 가자!")
else:
    print("남는 게 돈이야 택시타고 얼른가자!")
