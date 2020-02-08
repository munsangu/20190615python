# 파이썬은 리스트, 튜플, 딕셔너리는 전역변수
# 파이썬이 주력언어가 아닐 경우 -> 매개변수, 인자값 확인 확실하게 하기
def find_word(a): # a = dic
    # 내가 찾고 싶은 단어가 있다 -> 그 단어 검색
    # 내 딕셔너리에 있는 단어 -> 그 단어와 뜻을 출력
    # 내 딕셔너리에 없는 단어 -> 없는 단어입니다.
    word = input("단어 입력:")
    if word in a:
        print(word,":",a[word])
    else:
        print("없는 단어입니다.")
dic = {"apple":"사과", "banana":"바나나","cat":"고양이","dinosaur":"공룡","dog":"개"}
find_word(dic) # 인자값으로 딕셔너리 전달
