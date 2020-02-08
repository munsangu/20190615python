me = {"name":"moon", "phone":"010-9137-3632", "birth":"921223"} #name, phone, birth -> key / 나머지 value key:value
print(me)

print("\n===딕셔너리 생성/추가===")
#[]를 인덱싱이나 슬라이싱에 사용 => 딕셔너리만 예외
#딕셔너리변수["추가할 key값"] = 추가할 value 값
mart = {"다이제":2000}
mart["왕꿈틀이"] = 1000
print(mart)

mart["다이제"] = 2500
print(mart)

print("\n===딕셔너리 추가===")
# bank : 뜻이 여러개
# value 값에는 모든 자료형을 적을 수 있음
mart["츄파춥스"] = 2000
mart[999] = "999"
mart["우마이봉"] = [200, 300]
# key 값에는 단일 개체만 들어갈 수 있다.
# mart[["초코맛 우마이봉", "콘스프맛 우마이봉"]] = [200, 300]
print(mart)

print("\n===딕셔너리 삭제===")
# del list[인데스번호]
# del dict[key]
del mart ["다이제"]
print(mart)
