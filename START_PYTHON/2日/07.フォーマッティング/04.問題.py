kg = "KG ITBANK"
address = "부산광역시 수영구 민락동"
start = 16
name = "송진우"
end = 19
height = 170.2145
age = 29
Phone = "010 - 5567 - 1430"
#위의 변수를 이용하여 아래와 같이 출력

print("☆"*10+"KGITBANK"+"☆"*10)
print("파이썬 강의 : {0}시 ~ {1}시".format(start,end))
print("본인 이름 : {}".format(name))
print("본인 나이 : {}".format(age))
print("핸드폰 : %s"%Phone)
print("주소 : %s"%address)
print("키 : {:.2f}".format(height))
print("☆"*10+"KGITBANK"+"☆"*10)

#고급포매팅 소수점
#{인덱스번호:0.2f}
print("{:0.2f}".format(height))

#고급포매팅 간격
#{:<5} : 좌측정렬
#{:>5} : 우측정렬
#{:^10} : 가운데 정렬
print("이름 : {:<5}, 나이 : {:<3}".format("송진우",29))
print("이름 : {:>5}, 나이 : {:>3}".format("송진우",29))
print("이름 : {:^5}, 나이 : {:^3}".format("송진우",29))
