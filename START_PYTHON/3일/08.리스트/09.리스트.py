print("\n===요소 추가===")
#append는 하나의 요소 추가
a = [1,2,3]
a.append(4)
print(a)

print("\n===리스트 확장===")
#extend는 여러 요소 추가
a =[1,2,3]
a.extend([4,5])
print(a)

print("\n===정렬===")
a = [4,8,2,7,6]
a.sort() #오름차순 정렬<작은 것 => 큰것>
print(a)

a = ["i","t","b","a","n","k"]
a.sort()
print(a)

print("\n===뒤집기===")
a = ["a", "b","c","d","e"]
a.reverse()
print(a)

a = [4,8,2,7,6]
a.sort() # 오름차순 정렬
a.reverse() # 내림차순 정렬
print(a)

print("\n===위치찾기===")
# 문자열에서는 find, index
a = [1,2,3]
print(a.index(3))
print(a.index(1))

print("\n===요소 삽입===")
# insert(인덱스번호, 삽입할 데이터)
a = [1,2,3]
a.insert(0,4)
print(a)

print("\n===요소 제거===")
a = [1,2,3,1,2,3]
a.remove(2) # 왼쪽부터 찾아서 제일 처음만나는 것만 지움
print(a)
a.remove(2)
print(a)

print("\n===요소 끄집어내기===")
# 자료구조 => pop() => 데이터를 끄집어 냄
a = [1,2,3]
num = a.pop() #제일 오른쪽 요소를 끄집어와서 저장가능
print(a)
print("들고온 데이터 : %d"%num)

print("\n===요소 갯수 세기===")
a = [1,2,3,4,1]
print(a.count(1))
