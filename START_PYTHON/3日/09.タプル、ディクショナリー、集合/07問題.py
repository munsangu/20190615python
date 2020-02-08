print("\n===문제1===")
a = set([1,2,3,4,5,6])
b = set([4,5,6,7,8,9])
c = set([5,6,7,8,9,10])

num1 = tuple(a.intersection(b,c))
num2 = tuple(a.union(b,c))
num3 = tuple(a.difference(b,c))
print("교집합 : ", num1,"\n합집합 :", num2, "\n차집합 : ", num3)

print("\n===문제2===")
a = [1,1,5,5,4,3,6,7,2,1,5,5,8,5]
a = list(set(a))
print(a)

print("\n===문제3===")
d = set([1,2,3,4,5,6])
e = set([4,5,6,7,8,9])
f = set([5,6,7,8,9,10])
e.remove(4)
e.remove(5)
f.remove(5)
e.update([1,2])
print(d-e-f)
