#변수를 이용하여 포매팅 가능
num = 3
print("I eat %s cakes"%num)

print("\n===2개 이상의 포매팅===")
#2개 이상의 포맷문자 %() 괄호로 묶어줍니다.
print("I eat %s %s cakes"%(num, "cakes"))

print("\n===포매팅을 활용한 정렬===")
#%와 s사이에 양수로 적어주시면 그 숫자만큼 공간을 확보하고 우측정렬
print("%10s%5s"%("name","age"))
print("=" * 20)
print("%10s%5s"%("jinwoo","30"))
print("%10s%5s"%("donyu1","30"))
print("%10s%5s"%("bomin","22"))
print("=" * 20)
print("%-10s%-5s"%("jinwoo","30"))
print("%-10s%-5s"%("donyu1","30"))
print("%-10s%-5s"%("bomin","22"))

print("\n===포매팅을 활용한 소수점 표현===")
#%.2f : 소수점 2자리까지 표시
# 자료형을 모를땐 전부 %s => 단 소수점 표현빼고는...
a = 3.141592
print("%.2f"%a)
print("%.2s"%a)
