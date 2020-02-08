MonsterHP = 1000
turn = 0
while MonsterHP > 0:
    turn += 1
    print("[====={0}턴=====]".format(turn))
    print("어떤 기술을 사용하시겠습니까?")
    print("1: 기본공격\n2: 기술공격")
    skill = int(input("선택 : "))
    if skill == 1:
        print("몬스터에게 300의 데미지를 입혔습니다.")
        MonsterHP -= 300
    elif skill ==2:
        print("몬스터에게 300의 데미지를 입혔습니다.")
        MonsterHP -= 300
    else:
        print("잘못된 입력입니다.")
    print("몬스터 체력 : {0}\n".format(MonsterHP))
print("몬스터가 죽었습니다. ")
