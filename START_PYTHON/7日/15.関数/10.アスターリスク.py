# 애스터리스트(*)를 매개변수 앞에 붙여주면 인자의 갯수에 상관없이 전부 튜플로 저장
# args: argument의 약자 => 관례적으로 많이 사용
print("\n===== 인자의 갯수를 모르는 경우 =====")
def total(*args):
    print(args) # 튜플로 묶여 있음
    result = 0
    for i in args:
        result += i
    return result
print(total(1,2,3,4,5))
print(total(10,20,30,40,50,60,70,80,90))

print("\n===== 인자의 갯수를 모르는 경우2 =====")
 # ★ *는 반드시 매개변수의 가장 마지막에 사용해야 함.
def calc(oper, *args):
    if oper == '+':
        result = 0
        for i in args:
            result += i
    elif oper == '*':
        result = 1
        for i in args:
            result *= i
    return result
print(calc('+',1,2,3,4,5,))
print(calc('*',1,2,3,4,5))

print("\n===== 키워드 파라미터 =====")
# 애스터리스트(*)가 매개변수 앞에 두 개 붙음 => 딕셔너리 저장
# dict = {"key" : value ...}
def dict_kwargs(**kwargs):
    return kwargs
test_dict = dict_kwargs(rank1 = "jave", rank2 ="C", rank3="C++", rank4="Python")
print(test_dict)

print("\n===== 함수의 return =====")
# 1. 함수는 모든 코드를 다 읽으면 종료
# 2. return 명령어 만나면 종료
def calc(a,b):
    return a + b
    return a - b
print(calc(10,20))

print("\n===== 함수의 return2 =====")
# 1. 함수는 하나의 요소만 반환시킬 수 있음
def calc(a,b):
    return a + b, a - b # ,로 엮어주면 튜플이 됨
print(calc(10,20))

print("\n===== 함수의 디폴트매개변수 =====")
def r_c_p(i,you = "안냈다"): # you에게 "안냈다"라는 데이터를 저장
    if you == "안냈다":
        print("안냈으니까 내가 이겼다!")
        return # 함수 종료
    if i == you:
        print("비겼다")
    elif(i =="가위" and you == "바위") or (i == "바위" and you=="보")or(i == "보" and you =="가위"):
        print("내가 졌어")
    else:
        print("이겼어")
print("안내면 진거 가위바위보")
r_c_p("가위")
print("안내면 진거 가위바위보")
r_c_p("가위","바위") # you가 "안냈다"를 저장하고 있었는데 "바위"로 덮어씌워짐
