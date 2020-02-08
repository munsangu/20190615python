# 자료형
# int, float, str, bool
# list[], tuple(), dict{}, set([])
s1 = set([1,2,3])
s2 = set("Hello")
s3 = set(["Hello Python"])

print(s1)
print(s2)
print(s3)
# 집합은 순서없이 저장([]를 사용하면 순서가 있는 척을 해줌)
# 중복을 허용하지 않음
# 순서가 없다 => 인덱싱과 슬라이싱을 사용하지 못함

print("\n===교집합===")
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s3 = set([5,6,7,8,9,10])
#&, intersection()
print(s1 & s2 & s3)
print(s1.intersection(s2,s3))

print("\n===합집합===")
#|(shift + \), union
print( s1 | s2 | s3)
print(s1.union(s2,s3))

print("\n===차집합===")
#-, difference
print(s1-s2-s3)
print(s1.difference(s2,s3))

print("\n===요소 추가===")
s1 = set([1,2,3])
s1.add(4) #list의 append
print(s1)

s1.update([5,6,7]) #list의 extend
print(s1)

print("\n===요소 삭제===")
s1.remove(2)
print(s1)
