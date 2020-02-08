kor, eng, math = int(input("국어 : ")), int(input("영어: ")), int(input("수학: "))
# kor, eng, math에 0~100사이의 점수가 입력됬을때만 등급을 부여
# 범위를 벗어난 점수를 입력하면 잘못된 입력입니다. 출력

if kor <0 or kor >100 or eng<0 or eng>100 or math <0 or math>100:
    print("잘못된 입력입니다.")
elif (kor+eng+math)/3 >= 90:
    print("A등급")
elif (kor+eng+math)/3 >= 80:
    print("B등급")
elif (kor+eng+math)/3 >= 70:
    print("C등급")
elif (kor+eng+math)/3 >= 60:
    print("D등급")
else:
    print("F등급")
