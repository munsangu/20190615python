eng_dict ={"money" : "돈", "variable" : "변수", "function" : "함수", "recursive" : "반복적인"}
print(list(eng_dict.keys())) #key만 출력

answer = input("영어 단어 입력 : ")
# 이 영어단어가 내 딕셔너리에 있으면 뜻을 입력받고
# 그 영어단어의 뜻이 내가 입력한 뜻이 맞으면 정답니다!
if answer in eng_dict:
    mean = input("영어 단어 뜻 입력 : ")
    if mean == eng_dict[answer]:
        print(" 정답입니다. ")
    else:
        print("틀렸습니다.")
else: # 영어 사전에 단어가 없을 때
    print("사전에 없는 단어 입니다.")
