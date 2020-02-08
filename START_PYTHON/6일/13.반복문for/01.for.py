count = [0,1,2,3]

# num 변수에 count 리스트의 첫 번째 요소부터 마지막 요소까지 넣어주면서 반복
for num in count:
    print("num = %d"%num)

count = ["one","two","three","four"]

# 관례적으로 변수명을 i로 많이 사용
# i = "one"
# i = "two"
# i = "three"
# i = "four"
for i in count:
    print(i)

count.reverse()
for i in count:
    print(i)

jumsu = (90, 50, 60, 80, 40)
number = 1
for i in jumsu:
    if i >=60:
        print("%d번째 학생 합격!"%number)
    else:
        print("%d번째 학생 불합격!"%number)
    number+=1

# in []를 딕셔너리에 사용하면 key값으로만 조회
people = {"송새봄":29,"송여름":16,"송가을":32,"송겨울":5}
minor=[]
adult=[]
for i in people:
    if people[i] < 20:
        print("{0}님 : {1}살 ==> 미성년자".format(i,people[i]))
        minor.append(i)
    else:
        print("{0}님 : {1}살 ==> 성인".format(i,people[i]))
        adult.append(i)
print("성인 %s"%adult)
print("미성년자 %s"%minor)
