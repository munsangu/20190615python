Battle = int(input("대결 횟수: "))
count = 0
round = 1
ulist = [] # 학교리스트
dlist = [] # 술소비량리스트
while count < Battle:
    uni_input = int(input("%s회차 비교 학교 수 :"%round))
    while uni_input > 0:
        name = input("대학이름 : ")
        drink = int(input("술 소비량: "))
        ulist.append(name)
        dlist.append(drink)
        print("%s %s"%(name,drink))
        uni_input -=1
    count += 1 # 회차 증가
    Uindex = dlist.index(max(dlist)) # dlist에서 가장 큰 숫자의 인덱스 번호를 저장
    print("%s회차 승리: %s"%(round,ulist[Uindex]))
    round += 1 # 보여주는 회차 증가
    del dlist[:] # 리스트의 모든 요소 삭제
    del ulist[:]
