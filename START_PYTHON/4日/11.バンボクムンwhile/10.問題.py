import os
menu = {"콜라":1200,"사이다":1200,"조지아":1000,"컨피던스":600}
money = int(input("돈을 넣으세요 : "))
while True:
    print("========== 자판기 ==========")
    print("""
    콜라 : 1,200원
    사이다 : 1,200원
    조지아 : 1,000원
    컨피던스 : 600원
    >>종료
    """)
    choice = input("음료 입력: ")
    if choice == "종료":
        print("잔액 :%d"%money)
        print("자판기 프로그램을 종료합니다.")
        break
    elif choice not in menu:
        print("잘못된 입력입니다.")
    elif money >= menu[choice]:
        money -= menu[choice]
        print("%s를 구매했습니다."%choice)
        print("잔돈 : ",money)
    else:
        print("돈이 부족합니다.")

        os.system("pause")
        os.system("cls")
