people_skill = {"김연아":"피겨", "박지성":"축구","송진우":"강의","귀도_반_로섬":"파이썬"}
# 김연아의 특기를 알고 싶음
# 딕셔너리변수[key] : key값으로 옆의 value 값을 찾아옴
print(people_skill["김연아"])
# key 값을 이용하여 value를 변경
people_skill["김연아"] = "빵먹기"
# key값을 이용하여 추가
print(people_skill)
people_skill["이승우"] = "축구"
print(people_skill)

mart = {"다이제":800, "메로나":500, "코카콜라":700, "츄파츕스":200}
print("MarketO가 인수했어")
mart["다이제"] = 2200
print(mart)

print("\n===딕셔너리 주의사항===")
# key 값 중복 안됨
mart = {"다이제":2000, "메로나":500, "다이제":800}
print(mart)
