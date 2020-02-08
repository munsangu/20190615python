print("a" in ("a","b","c"))
print(7 in [1,2,3,4,5])
print("a" in "itbank")
# 딕셔너리는 key 값에만 찾습니다!
print("b" in {1:"a", 2:"b", 3:"c"})

pocket = ["phone", "card", "세종대왕"]
print("떡볶이를 먹고 싶은데 주머니에 현금이 있나?")

if "세종대왕" in pocket:
    print("떡튀순에 라면 추가")
else:
    print("현금인출기로 간다.")

print("="*30)
print("\t3의 배수 판별기")
print("="*30)

num = int(input("숫자 입력: "))

# 종속 문장 자리를 비워두면 에러가 발생
# 나중에 코드를 작성할 것이다. => pass
if num % 3 !=0:
    pass
else:
    print("3의 배수 입니다.")

if num % 3 ==0:
    print("3의 배수 입니다.")
