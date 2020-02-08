bus_cnt = int(input("정거장 수 : "))

if bus_cnt < 10:
    print("총 소요시간은 %s분 입니다."%(bus_cnt * 2))
else:
    #160분 // 60 => 2시간 40분
    if bus_cnt * 4 >= 60: #60분이 넘어가요
        hour = bus_cnt * 4 // 60 #시간을 저장
        min = bus_cnt *4 % 60   #분을 저장
        print("총 소요시간은 %s시 %s분 입니다."%(hour,min))
    else: #60분이 안넘어가요
        print("총 소요시간은 %s분 입니다."%(bus_cnt * 4))
