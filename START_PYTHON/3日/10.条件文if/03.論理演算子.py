gender = input("당신의 성별은[남/여]? : ")
age = int(input("당신의 나이는? : "))
genderlist =["남","여"]

# 프로그램 오류는 첫번째 프로그래머가 잘못된 코드를 짰을 경우
# 두번째는 사용자가 잘못된 방향으로 사용했을 경우
if gender in genderlist:
    if gender=="남" and age >= 19 and age < 150: # and(*) : 붙어있는 모든 조건식이 참이여야 참
        print("군대가자!")
    if gender=="여" or age < 19: # or(+) : 붙어있는 모든 조건식이 거짓만 아니면 참
        print("군대 안가도 되겠네")
else:
    print("잘못된 입력입니다.")
