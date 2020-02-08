import time as t
import random as r
def Quiz(w): #밖에서 단어리스트를 매개변수로 받습니다.
    #안에서 단어리스트를 random.choice를 이용해서 랜덤으로 하나씩 들고와서 저장하고
    #랜덤으로 들고온 단어의 첫글자만 보여주고 그 단어를 정확하게 맞추면
    #점수가 1점 증가되도록 함수를 만들어주세요
    #retrun 1 -> 1점 증가
    answer = r.choice(w)
    print(answer)
    player = input()
    if player == answer:
        print("맞췄습니다(+1점)")
        return 1
    else:
        print("틀렸습니다")
        return 0 #return 아무것도 안하면 None이 반환

w = ["apple","current","cake","blend","chat","game","python","language"]
score = 0
input("게임을 시작하려면 Enter키를 누르세요")
start = t.time()
while score < 5:
    print("="*10)
    print("점수 = {0}".format(score))
    #퀴즈 함수를 호출 -> score에 더해줍니다.
    score += Quiz(w)
end = t.time()
print("총 걸린 시간 : {0:.3f}초".format(end - start))
