import random # choice를 사용하기 위한 모듈
print("=== 랜덤 단어 맞추기 게임 ===")
wordlist = ["itbank","hello","dog","boy"]
# print(random.choice(wordlist))
# answer = random.choice(wordlist)

# int => 0 거짓
# list => [] 거짓

while wordlist: # wordlist에 요소가 있으면 계속 반복
    print(wordlist)
    answer = random.choice(wordlist)
    print(answer[0]) # 첫 번째 글자만 출력
    answer_input = input("단어 입력 : ")
    if answer_input == answer:
        print("정답입니다.")
        wordlist.remove(answer)
    else:
        print("오답입니다.")
print("★★★모두 맞췄습니다.★★★")
